from crypto_chassis_trade.core.exchange_base import ExchangeBase
from crypto_chassis_trade.core.models.instrument_information import InstrumentInformation
from crypto_chassis_trade.core.models.bbo import Bbo
from crypto_chassis_trade.core.models.trade import Trade
from crypto_chassis_trade.core.models.ohlcv import  Ohlcv
from crypto_chassis_trade.core.models.order import  Order, OrderStatus
from crypto_chassis_trade.core.models.fill import  Fill
from crypto_chassis_trade.core.models.balance import  Balance
from crypto_chassis_trade.core.models.position import  Position
from crypto_chassis_trade.helper import time_point_now
from crypto_chassis_trade.core.rest_request import RestRequest
from crypto_chassis_trade import logger
from crypto_chassis_trade.helper import convert_set_to_subsets,convert_unix_timestamp_milliseconds_to_time_point,round_to
import asyncio
import sys
import hashlib
import hmac
import base64
from datetime import datetime
from datetime import UTC


class Okx(ExchangeBase):
    INSTRUMENT_TYPE_SPOT = 'SPOT'
    INSTRUMENT_TYPE_MARGIN = 'MARGIN'
    INSTRUMENT_TYPE_SWAP = 'SWAP'
    INSTRUMENT_TYPE_FUTURES = 'FUTURES'
    INSTRUMENT_TYPE_OPTION = 'OPTION'
    def __init__(self, **kwargs):
        super().__init__(name='okx', **kwargs)
        self.rest_base_url = 'https://www.okx.com'
        self.rest_market_data_fetch_all_instrument_information_path = '/api/v5/public/instruments'
        self.rest_market_data_fetch_bbo_path = '/api/v5/market/tickers'
        self.rest_market_data_fetch_historical_trade_path = '/api/v5/market/history-trades'
        self.rest_market_data_fetch_historical_ohlcv_path = '/api/v5/market/history-candles'
        self.rest_account_create_order_path = '/api/v5/trade/order'
        self.rest_account_cancel_order_path = '/api/v5/trade/cancel-order'
        self.rest_account_fetch_order_path = '/api/v5/trade/order'
        self.rest_account_fetch_open_order_path = '/api/v5/trade/orders-pending'
        self.websocket_base_url = 'wss://ws.okx.com:8443' if not self.is_demo_trading else 'wss://wspap.okx.com:8443'
        self.websocket_market_data_path = '/ws/v5/public'
        self.websocket_market_data_path_2 = '/ws/v5/business'
        self.websocket_market_data_channel_bbo = 'bbo-tbt'
        self.websocket_market_data_channel_trade = 'trades'
        self.websocket_market_data_channel_ohlcv = 'candle'
        self.order_status_mapping = {
            'canceled':OrderStatus.CANCELED,
            'live':OrderStatus.NEW,
            'partially_filled':OrderStatus.PARTIALLY_FILLED,
            'filled':OrderStatus.FILLED,
            'mmp_canceled':OrderStatus.CANCELED,
        }
        self.broker_id='9cbc6a17a1fcBCDE'

    def validate_instrument_type(self,*,instrument_type):
        return instrument_type in {Okx.INSTRUMENT_TYPE_SPOT,Okx.INSTRUMENT_TYPE_MARGIN,Okx.INSTRUMENT_TYPE_SWAP, Okx.INSTRUMENT_TYPE_FUTURES,Okx.INSTRUMENT_TYPE_OPTION}

    def rest_market_data_fetch_all_instrument_information_create_rest_request_function(self):
        return self.rest_create_get_request_function(path=self.rest_market_data_fetch_all_instrument_information_path,query_params={'instType':self.instrument_type})

    def rest_market_data_fetch_bbo_create_rest_request_function(self):
        return self.rest_create_get_request_function(path=self.rest_market_data_fetch_bbo_path,query_params={'instType':self.instrument_type})

    def rest_market_data_fetch_historical_trade_create_rest_request_function(self,*,symbol):
        return self.rest_create_get_request_function(path=self.rest_market_data_fetch_historical_trade_path,query_params={'instId':symbol,'type':1})

    def rest_market_data_fetch_historical_ohlcv_create_rest_request_function(self,*,symbol):
        return self.rest_create_get_request_function(path=self.rest_market_data_fetch_historical_ohlcv_path,query_params={'instId':symbol,'after':(self.fetch_historical_ohlcv_end_unix_timestamp_seconds // self.ohlcv_interval_seconds * self.ohlcv_interval_seconds + self.ohlcv_interval_seconds)*1000,'bar':self.convert_ohlcv_interval_seconds_to_string(ohlcv_interval_seconds=self.ohlcv_interval_seconds),'limit':100})

    def rest_account_create_order_create_rest_request_function(self,*,order):
        if order.is_post_only:
            ord_type = 'post_only'
        elif order.is_fok:
            ord_type = 'fok'
        elif order.is_ioc:
            ord_type = 'ioc'
        elif order.limit_price:
            ord_type = 'limit'
        else:
            ord_type='market'

        json_payload = {
           'instId':order.symbol,
           'tdMode': self.margin_type or 'cash',
           'clOrdId': order.client_order_id,
           'side' : 'buy' if order.is_buy else 'sell',
           'ordType': ord_type,
           'sz': order.quantity,
            'tag':self.broker_id,
        }
        if order.limit_price:
            json_payload['px'] = order.limit_price
        if order.is_reduce_only:
            json_payload['reduceOnly'] = True
        if order.extra_params:
            json_payload.update(order.extra_params)
        return self.rest_create_post_request_function_with_signature(path=self.rest_account_create_order_path,json_payload=json_payload, json_serialize=self.json_serialize)

    def rest_account_cancel_order_create_rest_request_function(self,*,symbol,client_order_id):
        json_payload = {
           'instId':symbol,
           'clOrdId': client_order_id,
        }

        return self.rest_create_post_request_function_with_signature(path=self.rest_account_cancel_order_path,json_payload=json_payload, json_serialize=self.json_serialize)

    def rest_account_fetch_open_order_create_rest_request_function(self):
        return self.rest_create_get_request_function_with_signature(path=self.rest_account_fetch_open_order_path,query_params={'instType':self.instrument_type})

    def rest_account_fetch_order_create_rest_request_function(self,*,symbol,client_order_id):
        return self.rest_create_get_request_function_with_signature(path=self.rest_account_fetch_order_path,query_params={'instId':symbol,'clOrdId':client_order_id})

    def sign_request(self, *, rest_request, time_point):
        if rest_request.headers is None:
            rest_request.headers = {}
        headers = rest_request.headers
        headers['CONTENT-TYPE'] = 'application/json'
        headers['OK-ACCESS-KEY'] = self.api_key
        headers['OK-ACCESS-TIMESTAMP'] = f"{datetime.fromtimestamp(time_point[0], tz=UTC).strftime('%Y-%m-%dT%H:%M:%S')}.{str(time_point[1] // 1_000_000).zfill(3)}Z"
        headers['OK-ACCESS-PASSPHRASE'] = self.api_passphrase
        headers['OK-ACCESS-SIGN'] = base64.b64encode(hmac.new(bytes(self.api_secret, 'utf-8'), bytes(f"{headers['OK-ACCESS-TIMESTAMP']}{rest_request.method}{rest_request.path_with_query_params}{rest_request.payload or ''}", 'utf-8'), digestmod=hashlib.sha256).digest()).decode('utf-8')
        if self.is_demo_trading:
            headers['x-simulated-trading'] = '1'

    def is_rest_response_success(self,*,rest_response):
        return super().is_rest_response_success(rest_response=rest_response) and rest_response.json_deserialized_payload and rest_response.json_deserialized_payload["code"] == "0"

    def is_rest_response_for_all_instrument_information(self,*,rest_response):
        return rest_response.rest_request.path == self.rest_market_data_fetch_all_instrument_information_path

    def is_rest_response_for_bbo(self,*,rest_response):
        return rest_response.rest_request.path == self.rest_market_data_fetch_bbo_path

    def is_rest_response_for_historical_trade(self,*,rest_response):
        return rest_response.rest_request.path == self.rest_market_data_fetch_historical_trade_path

    def is_rest_response_for_historical_ohlcv(self,*,rest_response):
        return rest_response.rest_request.path == self.rest_market_data_fetch_historical_ohlcv_path

    def is_rest_response_for_create_order(self,*,rest_response):
        return rest_response.rest_request.path == self.rest_account_create_order_path and rest_response.rest_request.method == RestRequest.METHOD_POST

    def is_rest_response_for_cancel_order(self,*,rest_response):
        return rest_response.rest_request.path == self.rest_account_cancel_order_path

    def is_rest_response_for_fetch_order(self,*,rest_response):
        return rest_response.rest_request.path == self.rest_account_fetch_order_path and rest_response.rest_request.method == RestRequest.METHOD_GET

    def is_rest_response_for_fetch_open_order(self,*,rest_response):
        return rest_response.rest_request.path == self.rest_account_fetch_open_order_path

    def convert_rest_response_for_all_instrument_information(self,*,json_deserialized_payload,rest_request):
        return [InstrumentInformation(api_method=ExchangeBase.API_METHOD_REST,symbol=x['instId'],
    base_asset=x['baseCcy'],
    quote_asset=x['quoteCcy'],
    order_price_increment=x['tickSz'],
    order_quantity_increment=x['lotSz'],
    order_quantity_max=x['maxLmtSz'],
    order_quote_quantity_max=x['maxLmtAmt'],
    margin_asset=x['settleCcy'],
    underlying_symbol=x['uly'],
    contract_size=x['ctVal'],
    contract_multiplier=x['ctMult'],
    expiry_time=int(expTime)//1000 if (expTime:=x['expTime']) else None) for x in json_deserialized_payload['data']]

    def convert_rest_response_for_bbo(self,*,json_deserialized_payload,rest_request):
        return [Bbo(api_method=ExchangeBase.API_METHOD_REST,
        symbol=instId,
        exchange_update_time_point = convert_unix_timestamp_milliseconds_to_time_point(unix_timestamp_milliseconds=x['ts']),
        best_bid_price = x['bidPx'],
        best_bid_size = x['bidSz'],
        best_ask_price = x['askPx'],
        best_ask_size = x['askSz'],
    ) for x in json_deserialized_payload['data'] if (instId:=x['instId']) in self.symbols]

    def convert_rest_response_for_historical_trade(self,*,json_deserialized_payload,rest_request):
        return [Trade(api_method=ExchangeBase.API_METHOD_REST,symbol=x['instId'],
            exchange_update_time_point = convert_unix_timestamp_milliseconds_to_time_point(unix_timestamp_milliseconds=x['ts']),
            trade_id = int(x['tradeId']),
            price = x['px'],
            size = x['sz'],
            is_buyer_maker = x['side'] == 'sell',
        ) for x in json_deserialized_payload['data']]

    def convert_rest_response_for_historical_trade_to_next_rest_request_function(self,*,json_deserialized_payload,rest_request):
        data = json_deserialized_payload['data']
        if data:
            head = data[0]
            head_exchange_update_time_point = convert_unix_timestamp_milliseconds_to_time_point(unix_timestamp_milliseconds=head['ts'])
            head_trade_id = int(head['tradeId'])
            tail = data[-1]
            tail_exchange_update_time_point = convert_unix_timestamp_milliseconds_to_time_point(unix_timestamp_milliseconds=tail['ts'])
            tail_trade_id = int(tail['tradeId'])
            if (head_exchange_update_time_point, head_trade_id) < (tail_exchange_update_time_point, tail_trade_id):
                after = head_trade_id
                exchange_update_time_point = head_exchange_update_time_point
            else:
                after = tail_trade_id
                exchange_update_time_point = tail_exchange_update_time_point
            if self.fetch_historical_trade_start_unix_timestamp_seconds is None or exchange_update_time_point[0] >= self.fetch_historical_trade_start_unix_timestamp_seconds:
                return self.rest_create_get_request_function(path=self.rest_market_data_fetch_historical_trade_path,query_params={'instId':head['instId'],'type':1, 'after':after})

    def convert_rest_response_for_historical_ohlcv(self,*,json_deserialized_payload,rest_request):
        instId = rest_request.query_params['instId']
        return [Ohlcv(api_method=ExchangeBase.API_METHOD_REST,symbol=instId,
        start_unix_timestamp_seconds = int(x[0]) // 1000,
        open_price = x[1],
        high_price = x[2],
        low_price = x[3],
        close_price = x[4],
        volume = x[5],
        quote_volume = x[7],
    ) for x in json_deserialized_payload['data']]

    def convert_rest_response_for_historical_ohlcv_to_next_rest_request_function(self,*,json_deserialized_payload,rest_request):
        data = json_deserialized_payload['data']
        if data:
            head = data[0]
            head_ts = int(head[0])
            tail = data[-1]
            tail_ts = int(tail[0])
            if head_ts < tail_ts:
                after = head_ts
            else:
                after = tail_ts
            if self.fetch_historical_ohlcv_start_unix_timestamp_seconds is None or after // 1000 >= self.fetch_historical_ohlcv_start_unix_timestamp_seconds:
                return self.rest_create_get_request_function(path=self.rest_market_data_fetch_historical_ohlcv_path,query_params={'instId':rest_request.query_params['instId'],'after':after,'bar':self.convert_ohlcv_interval_seconds_to_string(ohlcv_interval_seconds=self.ohlcv_interval_seconds),'limit':100})

    def convert_rest_response_for_create_order(self,*,json_deserialized_payload,rest_request):
        x=json_deserialized_payload['data'][0]
        return Order(api_method=ExchangeBase.API_METHOD_REST,symbol=rest_request.json_payload['instId'],
        exchange_update_time_point = convert_unix_timestamp_milliseconds_to_time_point(unix_timestamp_milliseconds=x['ts']),
        order_id = x['ordId'],
        client_order_id = rest_request.json_payload['clOrdId'],
        exchange_create_time_point = convert_unix_timestamp_milliseconds_to_time_point(unix_timestamp_milliseconds=x['ts']),
        status = OrderStatus.CREATE_ACKNOWLEDGED,
    )

    def convert_rest_response_for_cancel_order(self,*,json_deserialized_payload,rest_request):
        x=json_deserialized_payload['data'][0]
        return Order(api_method=ExchangeBase.API_METHOD_REST,symbol=rest_request.json_payload['instId'],
        exchange_update_time_point = convert_unix_timestamp_milliseconds_to_time_point(unix_timestamp_milliseconds=x['ts']),
        client_order_id = rest_request.json_payload['clOrdId'],
        status = OrderStatus.CANCEL_ACKNOWLEDGED,
    )

    def convert_rest_response_for_fetch_order(self,*,json_deserialized_payload,rest_request):
        return self._extract_order_from_dict(input=json_deserialized_payload['data'][0])

    def convert_rest_response_for_fetch_open_order(self,*,json_deserialized_payload,rest_request):
        return [self._extract_order_from_dict(input=x) for x in json_deserialized_payload['data']]

    def convert_rest_response_for_fetch_open_order_to_next_rest_request_function(self,*,json_deserialized_payload,rest_request):
        data = json_deserialized_payload['data']
        if data:
            head = data[0]
            head_ord_id = head['ordId']
            tail = data[-1]
            tail_ord_id = tail['ordId']
            if head_ord_id < tail_ord_id:
                after = head_ord_id
            else:
                after = tail_ord_id
            return self.rest_create_get_request_function_with_signature(path=self.rest_account_fetch_open_order_path,query_params={'instType':self.instrument_type, 'after':after})

    async def handle_rest_response_for_error(self,*,rest_response):
        logger.error(f'rest_response = {rest_response}')
        if self.is_rest_response_for_create_order(rest_response=rest_response) or self.is_rest_response_for_cancel_order(rest_response=rest_response):
            await self.rest_account_fetch_order(symbol=rest_response.rest_request.json_payload['instId'],client_order_id=rest_response.rest_request.json_payload['clOrdId'])
        elif self.is_rest_response_for_fetch_order(rest_response=rest_response):
            print('is_rest_response_for_fetch_order')
            if rest_response.status_code == 200 and rest_response.json_deserialized_payload and rest_response.json_deserialized_payload.get('code') in {'51001', '51603'}:
                print('51001')
                print(f'self.orders = {self.orders}')
                self._replace_order(symbol=rest_response.rest_request.query_params['instId'],client_order_id=rest_response.rest_request.query_params['clOrdId'], exchange_update_time_point=time_point_now(), status=OrderStatus.REJECTED)

    async def websocket_market_data_connect(self):
        if self.symbols:
            if self.subscribe_bbo or self.subscribe_trade:
                await self.websocket_connect(base_url=self.websocket_base_url,path=self.websocket_market_data_path,query_params=self.websocket_market_data_query_params)
            if self.subscribe_ohlcv:
                await self.websocket_connect(base_url=self.websocket_base_url,path=self.websocket_market_data_path_2,query_params=self.websocket_market_data_query_params)

    async def handle_websocket_on_connected(self, *,websocket_connection):
        if websocket_connection.path == self.websocket_market_data_path:
            await self.websocket_market_data_subscribe_for_bbo_trade(websocket_connection=websocket_connection)
        elif websocket_connection.path == self.websocket_market_data_path_2:
            await self.websocket_market_data_subscribe_for_ohlcv(websocket_connection=websocket_connection)
        elif websocket_connection.path == self.websocket_account_path:
            await self.websocket_login(websocket_connection=websocket_connection)

    async def websocket_market_data_subscribe_for_bbo_trade(self,*,websocket_connection):
        symbols_subsets = convert_set_to_subsets(input=self.symbols, subset_length=self.websocket_market_data_channel_symbols_limit)
        logger.trace(f'symbols_subsets = {symbols_subsets}')
        for symbols_subset in symbols_subsets:
            await self.send_websocket_request(websocket_request=self.websocket_market_data_update_subscribe_create_websocket_request_for_bbo_trade(symbols=symbols_subset, is_subscribe=is_subscribe))
            await asyncio.sleep(self.websocket_market_data_channel_send_request_delay_seconds)

    async def websocket_market_data_subscribe_for_ohlcv(self,*,websocket_connection):
        symbols_subsets = convert_set_to_subsets(input=self.symbols, subset_length=self.websocket_market_data_channel_symbols_limit)
        logger.trace(f'symbols_subsets = {symbols_subsets}')
        for symbols_subset in symbols_subsets:
            await self.send_websocket_request(websocket_request=self.websocket_market_data_update_subscribe_create_websocket_request_for_ohlcv(symbols=symbols_subset, is_subscribe=is_subscribe))
            await asyncio.sleep(self.websocket_market_data_channel_send_request_delay_seconds)

    def websocket_login_create_websocket_request(self, *, time_point):
        arg = {}
        arg['apiKey'] = self.api_key
        arg['passphrase'] = self.api_passphrase
        arg['timestamp'] = str(time_point[0])
        arg['sign'] = base64.b64encode(hmac.new(bytes(self.api_secret, 'utf-8'), bytes(f"{arg['timestamp']}GET/users/self/verify", 'utf-8'), digestmod=hashlib.sha256).digest()).decode('utf-8')
        payload = self.json_serialize({
                    "op": "login",
                    "args": [arg],
                    })
        return self.websocket_create_request(path=self.websocket_account_path, payload=payload)


    def websocket_account_update_subscribe_create_websocket_request(self, *, is_subscribe):
        args = []
        if self.subscribe_order or self.subscribe_fill:
            args.append({
                "channel": "orders",
                "instType": f'{self.instrument_type}',
            })
        if self.subscribe_balance:
            args.append({
                "channel": "balance_and_position",
                "instType": f'{self.instrument_type}',
            })
        if self.subscribe_position:
            args.append({
                "channel": "positions",
                "instType": f'{self.instrument_type}',
            })
        payload = self.json_serialize({
                    "op": "subscribe",
                    "args": args
                    })
        return self.websocket_create_request(path=self.websocket_account_path, payload=payload)

    def websocket_market_data_update_subscribe_create_websocket_request_for_bbo_trade(self, *, symbols, is_subscribe):
        args = []
        for symbol in symbols:
            if self.subscribe_bbo:
                args.append({
                    'channel':self.websocket_market_data_channel_bbo,
                    'instId':symbol
                })
            if self.subscribe_trade:
                args.append({
                    'channel':self.websocket_market_data_channel_trade,
                    'instId':symbol
                })
        payload = self.json_serialize({
                    "op": "subscribe",
                    "args": args
                    })
        return self.websocket_create_request(path=self.websocket_market_data_path, payload=payload)

    def websocket_market_data_update_subscribe_create_websocket_request_for_ohlcv(self, *, symbols, is_subscribe):
        args = []
        for symbol in self.symbols:
            args.append({
                'channel':self.websocket_market_data_channel_ohlcv + self.convert_ohlcv_interval_seconds_to_string(ohlcv_interval_seconds=self.ohlcv_interval_seconds),
                'instId':symbol
            })
        payload = self.json_serialize({
                    "op": "subscribe",
                    "args": args
                    })
        return self.websocket_create_request(path=self.websocket_market_data_path_2, payload=payload)

    def convert_ohlcv_interval_seconds_to_string(self, *, ohlcv_interval_seconds):
        if ohlcv_interval_seconds < 60:
            return f'{ohlcv_interval_seconds}s'
        elif ohlcv_interval_seconds < 3600:
            return f'{ohlcv_interval_seconds//60}m'
        elif ohlcv_interval_seconds < 86400:
            return f'{ohlcv_interval_seconds//3600}H'
        else :
            return f'{ohlcv_interval_seconds//86400}D'

    def convert_ohlcv_interval_string_to_seconds(self, *, ohlcv_interval_string):
        unit_seconds = 0
        last_char = ohlcv_interval_string[-1]
        if last_char == 's':
            unit_seconds = 1
        elif last_char == 'm':
            unit_seconds = 60
        elif last_char == 'H':
            unit_seconds = 3600
        else:
            unit_seconds = 86400
        return int(ohlcv_interval_string[:-1]) * unit_seconds

    def websocket_on_message_extract_data(self,*,websocket_message):
        json_deserialized_payload = websocket_message.json_deserialized_payload
        websocket_message.payload_summary = {
            "event":json_deserialized_payload.get('event'),
            'op':json_deserialized_payload.get('op'),
            'channel': json_deserialized_payload.get('arg',{}).get('channel'),
            'code':json_deserialized_payload.get('code'),
        }
        id_ = json_deserialized_payload.get('id')
        websocket_message.websocket_request_id = id_
        if id_:
            websocket_message.websocket_request = self._websocket_requests.get(id_)
        return websocket_message

    def is_websocket_push_data(self, *, json_deserialized_payload,payload_summary):
        return payload_summary['event'] is None and payload_summary['op'] is None

    def is_websocket_push_data_for_bbo(self, *, json_deserialized_payload,payload_summary):
        return payload_summary["channel"] == self.websocket_market_data_channel_bbo


    def is_websocket_response_success(self, *, json_deserialized_payload,payload_summary):
        return  payload_summary['event'] != 'error' or payload_summary['code'] == '0'

    def is_websocket_response_for_subscribe(self, *, json_deserialized_payload,payload_summary):
        return payload_summary['event'] and payload_summary['event'] == 'subscribe'

    async def create_websocket_response(self, *, url, raw_websocket_response):
        # "pong" isn't valid json, only "\"pong\"" is valid json
        if raw_websocket_response.data == "pong":
            return WebsocketResponse(payload=raw_websocket_response.data)
        else:
            return await ExchangeBase.create_websocket_response(self, url=url,raw_websocket_response=raw_websocket_response)

    def convert_websocket_response_for_bbo(self,*,json_deserialized_payload):
        instId = json_deserialized_payload['arg']['instId']
        return [Bbo(api_method=ExchangeBase.API_METHOD_WEBSOCKET,
        symbol=instId,
        exchange_update_time_point = convert_unix_timestamp_milliseconds_to_time_point(unix_timestamp_milliseconds=x['ts']),
        best_bid_price = str(x['bids'][0][0]) if x['bids'] else None,
        best_bid_size = str(x['bids'][0][1]) if x['bids'] else None,
        best_ask_price = str(x['asks'][0][0]) if x['asks'] else None,
        best_ask_size = str(x['asks'][0][1]) if x['asks'] else None,
    ) for x in json_deserialized_payload['data']]

    def is_websocket_push_data_for_trade(self, *, json_deserialized_payload,payload_summary):
        return payload_summary["channel"] == self.websocket_market_data_channel_trade

    def convert_websocket_response_for_trade(self,*,json_deserialized_payload):
        instId = json_deserialized_payload['arg']['instId']
        return [Trade(api_method=ExchangeBase.API_METHOD_WEBSOCKET,symbol=instId,
        exchange_update_time_point = convert_unix_timestamp_milliseconds_to_time_point(unix_timestamp_milliseconds=x['ts']),
        trade_id = int(x['tradeId']),
        price = str(x['px']),
        size = str(x['sz']),
        is_buyer_maker = x['side'] == 'sell',
    ) for x in json_deserialized_payload['data']]

    def is_websocket_push_data_for_ohlcv(self, *, json_deserialized_payload,payload_summary):
        return payload_summary["channel"].startswith(self.websocket_market_data_channel_ohlcv)

    def convert_websocket_response_for_ohlcv(self,*,json_deserialized_payload):
        channel = json_deserialized_payload['arg']['channel']
        instId = json_deserialized_payload['arg']['instId']
        return [Ohlcv(api_method=ExchangeBase.API_METHOD_WEBSOCKET,symbol=instId,
        start_unix_timestamp_seconds = int(x[0]) // 1000,
        open_price = str(x[1]),
        high_price = str(x[2]),
        low_price = str(x[3]),
        close_price = str(x[4]),
        volume = str(x[5]),
        quote_volume = str(x[7]),
    ) for x in json_deserialized_payload['data']]


    def _extract_order_from_dict(self,*,input):
        return Order(api_method=ExchangeBase.API_METHOD_REST,symbol=input['instId'],
        exchange_update_time_point = convert_unix_timestamp_milliseconds_to_time_point(unix_timestamp_milliseconds=input['uTime']),
        order_id = input['ordId'],
        client_order_id = input['clOrdId'],
        is_buy = input['side'] == 'buy',
        limit_price = str(input['px']) or None,
        quantity = str(input['sz']),
        is_post_only = input['ordType'] == 'post_only',
        is_fok = input['ordType'] == 'fok',
        is_ioc = input['ordType'] == 'ioc',
        is_reduce_only = input['reduceOnly'] == 'true',
        cumulative_filled_quantity = str(input['accFillSz']) or None,
        cumulative_filled_quote_quantity = '{0:f}'.format(Decimal(input['avgPx']) * Decimal(input['accFillSz'])) if input['avgPx'] else None,
        exchange_create_time_point = convert_unix_timestamp_milliseconds_to_time_point(unix_timestamp_milliseconds=input['cTime']),
        status = self.order_status_mapping.get(input['state']),
        )
