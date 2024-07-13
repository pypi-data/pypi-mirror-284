import aiohttp
import asyncio
from crypto_chassis_trade.core.rest_request import RestRequest
from crypto_chassis_trade.core.rest_response import RestResponse
from crypto_chassis_trade.core.websocket_request import WebsocketRequest
from crypto_chassis_trade.core.websocket_message import WebsocketMessage
from crypto_chassis_trade.core.websocket_connection import WebsocketConnection
from crypto_chassis_trade import logger
from crypto_chassis_trade.helper import time_point_now
from crypto_chassis_trade.core.models.order import  Order,OrderStatus
import time
from crypto_chassis_trade.helper import create_url, json_serialize_pretty

import dataclasses
import functools
from itertools import groupby
from contextlib import suppress
from crypto_chassis_trade.helper import time_point_now,convert_set_to_subsets,get_base_url_from_url
class ExchangeBase:
    API_METHOD_REST = 'rest'
    API_METHOD_WEBSOCKET = 'websocket'
    MARGIN_TYPE_ISOLATED = 'isolated'
    MARGIN_TYPE_CROSS = 'cross'

    def __init__(self, *, name, instrument_type=None, symbols=None, fetch_all_instrument_information=True, subscribe_bbo=True, subscribe_trade=True, fetch_historical_trade=False,
    fetch_historical_trade_start_unix_timestamp_seconds = None,
    fetch_historical_trade_end_unix_timestamp_seconds = None,
    keep_historical_trade_seconds = 300,
    prune_historical_trade_interval_seconds = 60,
    ohlcv_interval_seconds=60,
    subscribe_ohlcv=True, fetch_historical_ohlcv=False,fetch_historical_ohlcv_start_unix_timestamp_seconds=None,
    fetch_historical_ohlcv_end_unix_timestamp_seconds=None,
    keep_historical_ohlcv_seconds = 300,
    prune_historical_ohlcv_interval_seconds = 60,
    account_type=None,api_key=None, api_secret=None, api_passphrase=None, is_demo_trading=False, margin_type=None, subscribe_order=True,fetch_historical_order=False,
    keep_historical_order_seconds = 300,
    prune_historical_order_interval_seconds = 60,
    subscribe_fill=True, fetch_historical_fill=False,
    keep_historical_fill_seconds = 300,
    prune_historical_fill_interval_seconds = 60,
    subscribe_balance=True,subscribe_position=True,
    extra_data=None,
    json_serialize=None, json_serialize_pretty=json_serialize_pretty, json_deserialize=None,
    websocket_connection_heartbeat_period_seconds=10,
    websocket_connection_auto_reconnect=True,
    rest_market_data_fetch_all_instrument_information_period_seconds=300,
    rest_market_data_fetch_bbo_period_seconds=300,
    rest_account_check_open_order_period_seconds=60,
    rest_account_check_open_order_threshold_seconds=60,
    rest_account_check_sent_order_period_seconds=10,
    rest_account_check_sent_order_threshold_seconds=10,
    rest_account_fetch_balance_period_seconds=60,
    rest_account_fetch_position_period_seconds=60,
    rest_market_data_send_request_delay_seconds=0.05,
    rest_account_send_request_delay_seconds=0.05,
    websocket_market_data_channel_symbols_limit = 50,
    websocket_market_data_channel_send_request_delay_seconds=0.05,
    websocket_account_channel_send_request_delay_seconds=0.05,
    trade_api_method_preference = API_METHOD_REST,
    ):
        now_unix_timestamp_seconds = int(time.time())
        now_unix_timestamp_milliseconds = now_unix_timestamp_seconds * 1000
        self.name = name
        self.instrument_type = instrument_type
        if not self.validate_instrument_type(instrument_type=instrument_type):
            logger.critical(Exception(f"invalid instrument_type {instrument_type} for exchange {self.name}"))
        self.symbols = symbols
        self.fetch_all_instrument_information = fetch_all_instrument_information
        self.subscribe_bbo = subscribe_bbo
        self.subscribe_trade = subscribe_trade
        self.fetch_historical_trade = fetch_historical_trade
        self.fetch_historical_trade_start_unix_timestamp_seconds=fetch_historical_trade_start_unix_timestamp_seconds
        self.fetch_historical_trade_end_unix_timestamp_seconds=fetch_historical_trade_end_unix_timestamp_seconds if fetch_historical_trade_end_unix_timestamp_seconds is not None else now_unix_timestamp_seconds
        self.keep_historical_trade_seconds=keep_historical_trade_seconds
        self.prune_historical_trade_interval_seconds = prune_historical_trade_interval_seconds
        self.ohlcv_interval_seconds=ohlcv_interval_seconds
        self.subscribe_ohlcv=subscribe_ohlcv
        self.fetch_historical_ohlcv=fetch_historical_ohlcv
        self.fetch_historical_ohlcv_start_unix_timestamp_seconds=fetch_historical_ohlcv_start_unix_timestamp_seconds
        self.fetch_historical_ohlcv_end_unix_timestamp_seconds=fetch_historical_ohlcv_end_unix_timestamp_seconds if fetch_historical_ohlcv_end_unix_timestamp_seconds is not None else now_unix_timestamp_seconds
        self.keep_historical_ohlcv_seconds=keep_historical_ohlcv_seconds
        self.prune_historical_ohlcv_interval_seconds = prune_historical_ohlcv_interval_seconds

        self.account_type=account_type
        self.api_key=api_key
        self.api_secret=api_secret
        self.api_passphrase=api_passphrase
        self.is_demo_trading=is_demo_trading
        self.margin_type = margin_type

        self.subscribe_order=subscribe_order
        self.fetch_historical_order=fetch_historical_order
        self.keep_historical_order_seconds = keep_historical_order_seconds
        self.prune_historical_order_interval_seconds = prune_historical_order_interval_seconds
        self.subscribe_fill=subscribe_fill
        self.fetch_historical_fill=fetch_historical_fill
        self.keep_historical_fill_seconds = keep_historical_fill_seconds
        self.prune_historical_fill_interval_seconds = prune_historical_fill_interval_seconds
        self.subscribe_balance=subscribe_balance
        self.subscribe_position=subscribe_position

        self.extra_data=extra_data

        self.client_session = None
        if json_serialize:
            self.json_serialize = json_serialize
        else:
            import json
            self.json_serialize = json.dumps

        self.json_serialize_pretty = json_serialize_pretty

        if json_deserialize:
            self.json_deserialize = json_deserialize
        else:
            import json
            self.json_deserialize = functools.partial(json.loads, parse_float = lambda x : x, parse_int = lambda x : x)



        self.all_instrument_information = {}
        self.bbos = {}
        self.trades = {}
        self.ohlcvs = {}
        self.orders = {}
        self.fills = {}
        self.balances = {}
        self.positions = {}

        self._websocket_connections = {}
        # self._websocket_request_buffers = {}
        self._websocket_reconnect_delay_seconds = {}
        self._websocket_logged_in_connections = set()
        self._websocket_requests = {}
        self.websocket_connection_heartbeat_period_seconds = websocket_connection_heartbeat_period_seconds
        self.websocket_connection_auto_reconnect = websocket_connection_auto_reconnect
        self.rest_market_data_fetch_all_instrument_information_period_seconds = rest_market_data_fetch_all_instrument_information_period_seconds
        self.rest_market_data_fetch_bbo_period_seconds = rest_market_data_fetch_bbo_period_seconds
        self.rest_market_data_send_request_delay_seconds = rest_market_data_send_request_delay_seconds
        self.rest_account_send_request_delay_seconds = rest_account_send_request_delay_seconds
        self.rest_account_check_open_order_period_seconds = rest_account_check_open_order_period_seconds
        self.rest_account_check_open_order_threshold_seconds = rest_account_check_open_order_threshold_seconds
        self.rest_account_check_sent_order_period_seconds = rest_account_check_sent_order_period_seconds

        self._next_rest_request_id_int = 0
        self._next_websocket_request_id_int = 0
        self._next_client_order_id_int = now_unix_timestamp_milliseconds
        self.rest_base_url = None
        self.rest_market_data_fetch_all_instrument_information_path = None
        self.rest_market_data_fetch_bbo_path = None
        self.rest_market_data_fetch_historical_trade_path = None
        self.rest_market_data_fetch_historical_ohlcv_path = None
        self.rest_account_create_order_path = None
        self.rest_account_cancel_order_path = None
        self.rest_account_fetch_order_path = None
        self.rest_account_fetch_open_order_path = None
        self.websocket_base_url = None
        self.websocket_market_data_path = None
        self.websocket_market_data_query_params = None
        self.websocket_account_path = None
        self.websocket_account_query_params = None

        self._all_tasks = set()

        self.websocket_market_data_channel_symbols_limit = websocket_market_data_channel_symbols_limit
        self.websocket_market_data_channel_send_request_delay_seconds = websocket_market_data_channel_send_request_delay_seconds
        self.websocket_account_channel_send_request_delay_seconds = websocket_account_channel_send_request_delay_seconds
        self.trade_api_method_preference = trade_api_method_preference
        self.websocket_market_data_channel_bbo = None
        self.websocket_market_data_channel_trade = None
        self.websocket_market_data_channel_ohlcv = None

        self.order_status_mapping = {}

        self.broker_id = None

    @property
    def websocket_connections(self):
        return self._websocket_connections



    def validate_instrument_type(self,*,instrument_type):
        return True

    async def websocket_connect(self,*,base_url,path, query_params):
        try:
            while True:
                url = create_url(base_url=base_url,path=path)
                async with self.client_session.ws_connect(url, params=query_params, heartbeat=self.websocket_connection_heartbeat_period_seconds) as client_websocket_response:
                    websocket_connection = WebsocketConnection(base_url=base_url,path=path,query_params=query_params,connection=client_websocket_response)
                    await self.websocket_on_connected(websocket_connection=websocket_connection)
                    async for raw_websocket_message in websocket_connection:
                        if raw_websocket_message.type == aiohttp.WSMsgType.TEXT:
                            logger.trace(raw_websocket_message.data)
                            try:
                                await self.websocket_on_message(base_url=base_url,path=path, query_params=query_params,websocket_connection=websocket_connection,raw_websocket_message_data=raw_websocket_message.data)
                            except Exception as exception:
                                logger.error(exception)

                        elif raw_websocket_message.type == aiohttp.WSMsgType.ERROR:
                            logger.error(websocket_connection.exception())
                            break
                    exception = websocket_connection.exception() if websocket_connection.exception() else Exception(f"websocket connection closed: close code = {websocket_connection.close_code()}")
                    # close reason
                    logger.error(exception)
                self._websocket_connections.pop((base_url,path, query_params), None)
                # self._websocket_request_buffers.pop(url, None)
                self._websocket_logged_in_connections.discard((base_url,path, query_params))
                await self.websocket_on_disconnected(websocket_connection=websocket_connection)
                if self.websocket_connection_auto_reconnect:
                    asyncio.sleep(self.get_websocket_reconnect_delay_seconds(websocket_connection=websocket_connection))
                else:
                    break

        except Exception as exception:
            logger.error(exception)

    async def start(self,*,client_session=None):
        self.client_session = client_session if client_session else  aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False))
        if self.fetch_all_instrument_information:
            await self.rest_market_data_fetch_all_instrument_information()
            if self.rest_market_data_fetch_all_instrument_information_period_seconds > 0:
                async def start_periodic_rest_market_data_fetch_all_instrument_information():
                    try:
                        while True:
                            await asyncio.sleep(self.rest_market_data_fetch_all_instrument_information_period_seconds)
                            await self.rest_market_data_fetch_all_instrument_information()
                    except Exception as exception:
                        logger.error(exception)
                self._all_tasks.add(asyncio.create_task(start_periodic_rest_market_data_fetch_all_instrument_information()))
        if self.subscribe_bbo:
            await self.rest_market_data_fetch_bbo()
            if self.rest_market_data_fetch_bbo_period_seconds is not None and self.rest_market_data_fetch_bbo_period_seconds > 0:
                async def start_periodic_rest_market_data_fetch_bbo():
                    try:
                        while True:
                            await asyncio.sleep(self.rest_market_data_fetch_bbo_period_seconds)
                            await self.rest_market_data_fetch_bbo()
                    except Exception as exception:
                        logger.error(exception)
                self._all_tasks.add(asyncio.create_task(start_periodic_rest_market_data_fetch_bbo()))

        if self.subscribe_order:
            await self.rest_account_fetch_open_order()
            if self.rest_account_check_open_order_period_seconds is not None and self.rest_account_check_open_order_period_seconds > 0:
                async def start_periodic_rest_account_check_open_order():
                    try:
                        while True:
                            await asyncio.sleep(self.rest_account_check_open_order_period_seconds)
                            await self.rest_account_check_open_order()
                    except Exception as exception:
                        logger.error(exception)
                self._all_tasks.add(asyncio.create_task(start_periodic_rest_account_check_open_order()))

            if self.rest_account_check_sent_order_period_seconds is not None and self.rest_account_check_sent_order_period_seconds > 0:
                async def start_periodic_rest_account_check_sent_order():
                    try:
                        while True:
                            await asyncio.sleep(self.rest_account_check_sent_order_period_seconds)
                            await self.rest_account_check_sent_order()
                    except Exception as exception:
                        logger.error(exception)
                self._all_tasks.add(asyncio.create_task(start_periodic_rest_account_check_sent_order()))

        if self.subscribe_balance:
            await self.rest_account_fetch_balance()
            if self.rest_account_fetch_balance_period_seconds is not None and self.rest_account_fetch_balance_period_seconds > 0:
                async def start_periodic_rest_account_fetch_balance():
                    try:
                        while True:
                            await asyncio.sleep(self.rest_account_fetch_balance_period_seconds)
                            await self.rest_account_fetch_balance()
                    except Exception as exception:
                        logger.error(exception)
                self._all_tasks.add(asyncio.create_task(start_periodic_rest_account_fetch_balance()))

        if self.subscribe_position:
            await self.rest_account_fetch_position()
            if self.rest_account_fetch_position_period_seconds is not None and self.rest_account_fetch_position_period_seconds > 0:
                async def start_periodic_rest_account_fetch_position():
                    try:
                        while True:
                            await asyncio.sleep(self.rest_account_fetch_position_period_seconds)
                            await self.rest_account_fetch_position()
                    except Exception as exception:
                        logger.error(exception)
                self._all_tasks.add(asyncio.create_task(start_periodic_rest_account_fetch_position()))

        if self.prune_historical_trade_interval_seconds is not None and self.prune_historical_trade_interval_seconds > 0:
            async def start_periodic_prune_historical_trade():
                try:
                    while True:
                        await asyncio.sleep(self.prune_historical_trade_interval_seconds)
                        self.prune_trades()
                except Exception as exception:
                    logger.error(exception)
            self._all_tasks.add(asyncio.create_task(start_periodic_prune_historical_trade()))

        if self.prune_historical_ohlcv_interval_seconds is not None and self.prune_historical_ohlcv_interval_seconds > 0:
            async def start_periodic_prune_historical_ohlcv():
                try:
                    while True:
                        await asyncio.sleep(self.prune_historical_ohlcv_interval_seconds)
                        self.prune_ohlcvs()
                except Exception as exception:
                    logger.error(exception)
            self._all_tasks.add(asyncio.create_task(start_periodic_prune_historical_ohlcv()))

        if self.prune_historical_order_interval_seconds is not None and self.prune_historical_order_interval_seconds > 0:
            async def start_periodic_prune_historical_order():
                try:
                    while True:
                        await asyncio.sleep(self.prune_historical_order_interval_seconds)
                        self.prune_orders()
                except Exception as exception:
                    logger.error(exception)
            self._all_tasks.add(asyncio.create_task(start_periodic_prune_historical_order()))

        if self.prune_historical_fill_interval_seconds is not None and self.prune_historical_fill_interval_seconds > 0:
            async def start_periodic_prune_historical_fill():
                try:
                    while True:
                        await asyncio.sleep(self.prune_historical_fill_interval_seconds)
                        self.prune_fills()
                except Exception as exception:
                    logger.error(exception)
            self._all_tasks.add(asyncio.create_task(start_periodic_prune_historical_fill()))

        await asyncio.gather(
            self.websocket_market_data_connect(),
            self.websocket_account_connect()
        )

        await asyncio.gather(
            self.rest_market_data_fetch_historical_data()
            # self.rest_account_fetch_historical_data()
        )

    async def rest_market_data_fetch_historical_data(self):
        for symbol in sorted(self.symbols):
            if self.fetch_historical_trade:
                await self.rest_market_data_fetch_historical_trade(symbol=symbol)
            if self.fetch_historical_ohlcv:
                await self.rest_market_data_fetch_historical_ohlcv(symbol=symbol)

    async def rest_market_data_fetch_historical_trade(self, *, symbol):
        await self.send_rest_request(rest_request_function=self.rest_market_data_fetch_historical_trade_create_rest_request_function(symbol=symbol))

    async def rest_market_data_fetch_historical_ohlcv(self, *, symbol):
        await self.send_rest_request(rest_request_function=self.rest_market_data_fetch_historical_ohlcv_create_rest_request_function(symbol=symbol))

    async def stop(self):
        for task in self._all_tasks:
            task.cancel()
        await asyncio.gather(*self._all_tasks, return_exceptions=True)
        # disconnect all ws connections

    async def restart(self,*,client_session=None):
        await self.stop()
        await self.client_session.close()
        self.client_session = None
        await asyncio.sleep(1)
        await self.start(client_session=client_session)

    async def rest_account_fetch_order(self,*,symbol,client_order_id):
        await self.send_rest_request(rest_request_function=self.rest_account_fetch_order_create_rest_request_function(symbol=symbol,client_order_id=client_order_id))

    async def rest_account_fetch_open_order(self):
        await self.send_rest_request(rest_request_function=self.rest_account_fetch_open_order_create_rest_request_function())

    async def rest_account_fetch_balance(self):
        await self.send_rest_request(rest_request_function=self.rest_account_fetch_balance_create_rest_request_function())

    async def rest_account_fetch_positon(self):
        await self.send_rest_request(rest_request_function=self.rest_account_fetch_position_create_rest_request_function())

    def create_order(self, *, order, trade_api_method_preference=None):
        order_to_create = order
        if not order_to_create.client_order_id:
            order_to_create = dataclasses.replace(order, exchange_update_time_point=time_point_now(), status=OrderStatus.CREATE_SENT, client_order_id=self.create_next_client_order_id())
        else:
            order_to_create = dataclasses.replace(order, exchange_update_time_point=time_point_now(), status=OrderStatus.CREATE_SENT)
        self._upsert_order(order=order_to_create)

        if (trade_api_method_preference is None and self.trade_api_method_preference == ExchangeBase.API_METHOD_REST) or trade_api_method_preference == ExchangeBase.API_METHOD_REST:
            self._all_tasks.add(asyncio.create_task(self.start_rest_account_create_order(order=order_to_create)))
        else:
            pass
        return order_to_create

    async def rest_account_create_order(self, *, order):
        await self.send_rest_request(rest_request_function=self.rest_account_create_order_create_rest_request_function(order=order))

    async def start_rest_account_create_order(self, *,order):
        try:
            await self.rest_account_create_order(order=order)
        except Exception as exception:
            logger.error(exception)

    def cancel_order(self, *, symbol, client_order_id, trade_api_method_preference=None):
        self._replace_order(symbol=symbol,client_order_id=client_order_id,exchange_update_time_point=time_point_now(),status=OrderStatus.CANCEL_SENT)

        if (trade_api_method_preference is None and self.trade_api_method_preference == ExchangeBase.API_METHOD_REST) or trade_api_method_preference == ExchangeBase.API_METHOD_REST:
            self._all_tasks.add(asyncio.create_task(self.start_rest_account_cancel_order(symbol=symbol, client_order_id = client_order_id)))
        else:
            pass

    async def start_rest_account_cancel_order(self, *,symbol, client_order_id):
        try:
            await self.rest_account_cancel_order(symbol=symbol, client_order_id = client_order_id)
        except Exception as exception:
            logger.error(exception)

    async def rest_account_cancel_order(self, *, symbol, client_order_id):
        await self.send_rest_request(rest_request_function=self.rest_account_cancel_order_create_rest_request_function(symbol=symbol, client_order_id = client_order_id))

    def cancel_orders(self, *, symbol=None, trade_api_method_preference=None):
        if symbol and symbol in self.orders:
            for client_order_id, order in self.orders[symbol].items():
                if not order.is_sent:
                    self.orders[symbol][client_order_id] = dataclasses.replace(order, status=OrderStatus.CANCEL_SENT)
                    if (trade_api_method_preference is None and self.trade_api_method_preference == ExchangeBase.API_METHOD_REST) or trade_api_method_preference == ExchangeBase.API_METHOD_REST:
                        self._all_tasks.add(asyncio.create_task(self.start_rest_account_cancel_order(symbol=symbol, client_order_id=client_order_id)))
                    else:
                        pass
        else:
            for symbol, orders_for_symbol in self.orders.items():
                for client_order_id, order in orders_for_symbol.items():
                    if not order.is_sent:
                        self.orders[symbol][client_order_id] = dataclasses.replace(order, status=OrderStatus.CANCEL_SENT)
                        if (trade_api_method_preference is None and self.trade_api_method_preference == ExchangeBase.API_METHOD_REST) or trade_api_method_preference == ExchangeBase.API_METHOD_REST:
                            self._all_tasks.add(asyncio.create_task(self.start_rest_account_cancel_order(symbol=symbol, client_order_id=client_order_id)))
                        else:
                            pass



    async def rest_market_data_fetch_all_instrument_information(self):
        await self.send_rest_request(rest_request_function=self.rest_market_data_fetch_all_instrument_information_create_rest_request_function())

    async def rest_market_data_fetch_bbo(self):
        await self.send_rest_request(rest_request_function=self.rest_market_data_fetch_bbo_create_rest_request_function())

    def rest_market_data_fetch_all_instrument_information_create_rest_request_function(self):
        raise NotImplementedError

    def rest_market_data_fetch_bbo_create_rest_request_function(self):
        raise NotImplementedError

    def rest_market_data_fetch_historical_trade_create_rest_request_function(self,*,symbol):
        raise NotImplementedError

    def rest_market_data_fetch_historical_ohlcv_create_rest_request_function(self,*,symbol):
        raise NotImplementedError

    def rest_account_create_order_create_rest_request_function(self,*,order):
        raise NotImplementedError

    def rest_account_cancel_order_create_rest_request_function(self,*,symbol,client_order_id):
        raise NotImplementedError

    def rest_account_fetch_open_order_create_rest_request_function(self):
        raise NotImplementedError

    def rest_account_fetch_order_create_rest_request_function(self,*,symbol,client_order_id):
        raise NotImplementedError

    async def websocket_market_data_connect(self):
        if self.symbols and (self.subscribe_bbo or self.subscribe_trade or self.subscribe_ohlcv):
            await self.websocket_connect(base_url=self.websocket_base_url,path=self.websocket_market_data_path,query_params=self.websocket_market_data_query_params)

    async def websocket_account_connect(self):
        if self.subscribe_order or self.subscribe_fill or self.subscribe_balance or self.subscribe_position:
            await self.websocket_connect(base_url=self.websocket_base_url,path=self.websocket_account_path,query_params=self.websocket_account_query_params)





    async def websocket_account_update_subscribe(self,*,is_subscribe):
        if self.subscribe_order or self.subscribe_fill or self.subscribe_balance or self.subscribe_position:
            await self.send_websocket_request(websocket_request=self.websocket_market_data_update_subscribe_create_websocket_request(symbols=symbols_subset, is_subscribe=is_subscribe))
            await asyncio.sleep(self.websocket_account_channel_send_request_delay_seconds)

    # async def rest_market_data_fetch_history(self):
    #     if self.subscribe_bbo:
    #         await self.send_rest_request(rest_request=self.rest_market_data_fetch_bbo_create_rest_request_function())
    #     if self.subscribe_trade or self.fetch_historical_trade:
    #         await self.send_rest_request(rest_request=self.rest_market_data_fetch_trade_create_rest_request_function())
    #     if self.subscribe_ohlcv or self.fetch_historical_ohlcv:
    #         await self.send_rest_request(rest_request=self.rest_market_data_fetch_ohlcv_create_rest_request_function())

    async def websocket_private_data_update_subscribe(self):
        await self.send_websocket_request(self.websocket_private_data_update_subscribe_create_websocket_requests(is_subscribe=is_subscribe))

    # async def rest_private_data_fetch_history(self):
    #     pass

    async def send_rest_request(self, *, rest_request_function, delay_seconds=0, timeout_seconds = 10):
        logger.trace(f'delay_seconds = {delay_seconds}')
        next_rest_request_function = rest_request_function
        next_rest_request_delay_seconds = delay_seconds
        while True:
            if next_rest_request_delay_seconds > 0:
                await asyncio.sleep(next_rest_request_delay_seconds)
            rest_request = next_rest_request_function(time_point=time_point_now())
            logger.trace(f'rest_request = {self.json_serialize_pretty(rest_request.as_json())}')
            async with self.client_session.request(method=rest_request.method, url=rest_request.url, params=rest_request.query_params, data=rest_request.payload, headers=rest_request.headers, timeout=aiohttp.ClientTimeout(sock_read=timeout_seconds)) as client_response:
                # logger.trace(f'client_response = {client_response}')
                try:
                    rest_response = await self.rest_on_response(rest_request=rest_request, raw_rest_response=client_response)
                    if not rest_response or rest_response.next_rest_request_function is None:
                        break
                    else:
                        next_rest_request_function = rest_response.next_rest_request_function
                        next_rest_request_delay_seconds = rest_response.next_rest_request_delay_seconds
                except Exception as exception:
                    logger.error(exception)
                    break


    async def rest_on_response(self, *, rest_request, raw_rest_response):
        rest_response = RestResponse(rest_request=rest_request, status_code=raw_rest_response.status, payload=await raw_rest_response.text(), headers=raw_rest_response.headers,json_deserialize=self.json_deserialize)
        logger.trace(f'rest_response = {self.json_serialize_pretty(rest_response.as_json())}')
        json_deserialized_payload = rest_response.json_deserialized_payload
        if self.is_rest_response_success(rest_response=rest_response):
            if self.is_rest_response_for_all_instrument_information(rest_response=rest_response):
                await self.handle_rest_response_for_all_instrument_information(all_instrument_information=self.convert_rest_response_for_all_instrument_information(json_deserialized_payload=json_deserialized_payload,rest_request=rest_request))
            elif self.is_rest_response_for_bbo(rest_response=rest_response):
                await self.handle_rest_response_for_bbo(bbos=self.convert_rest_response_for_bbo(json_deserialized_payload=json_deserialized_payload,rest_request=rest_request))
            elif self.is_rest_response_for_historical_trade(rest_response=rest_response):
                await self.handle_rest_response_for_historical_trade(historical_trades=self.convert_rest_response_for_historical_trade(json_deserialized_payload=json_deserialized_payload,rest_request=rest_request))
                rest_response.next_rest_request_function = self.convert_rest_response_for_historical_trade_to_next_rest_request_function(json_deserialized_payload=json_deserialized_payload,rest_request=rest_request)
                rest_response.next_rest_request_delay_seconds = self.rest_market_data_send_request_delay_seconds
            elif self.is_rest_response_for_historical_ohlcv(rest_response=rest_response):
                await self.handle_rest_response_for_historical_ohlcv(historical_ohlcvs=self.convert_rest_response_for_historical_ohlcv(json_deserialized_payload=json_deserialized_payload,rest_request=rest_request))
                rest_response.next_rest_request_function = self.convert_rest_response_for_historical_ohlcv_to_next_rest_request_function(json_deserialized_payload=json_deserialized_payload,rest_request=rest_request)
                rest_response.next_rest_request_delay_seconds = self.rest_market_data_send_request_delay_seconds
            elif self.is_rest_response_for_create_order(rest_response=rest_response):
                await self.handle_rest_response_for_create_order(order=self.convert_rest_response_for_create_order(json_deserialized_payload=json_deserialized_payload,rest_request=rest_request))
            elif self.is_rest_response_for_cancel_order(rest_response=rest_response):
                await self.handle_rest_response_for_cancel_order(order=self.convert_rest_response_for_cancel_order(json_deserialized_payload=json_deserialized_payload,rest_request=rest_request))
            elif self.is_rest_response_for_fetch_order(rest_response=rest_response):
                await self.handle_rest_response_for_fetch_order(order=self.convert_rest_response_for_fetch_order(json_deserialized_payload=json_deserialized_payload,rest_request=rest_request))
            elif self.is_rest_response_for_fetch_open_order(rest_response=rest_response):
                await self.handle_rest_response_for_fetch_open_order(open_orders=self.convert_rest_response_for_fetch_open_order(json_deserialized_payload=json_deserialized_payload,rest_request=rest_request))
                rest_response.next_rest_request_function = self.convert_rest_response_for_fetch_open_order_to_next_rest_request_function(json_deserialized_payload=json_deserialized_payload,rest_request=rest_request)
                rest_response.next_rest_request_delay_seconds = self.rest_account_send_request_delay_seconds
        else:
            rest_response = await self.handle_rest_response_for_error(rest_response=rest_response)
        return rest_response

    async def websocket_on_connected(self,*,websocket_connection):
        logger.trace(f'websocket_connection = {websocket_connection}')
        self._websocket_connections[(base_url,path, query_params)] = websocket_connection
        # periodic ping/pong
        await self.handle_websocket_on_connected(websocket_connection=websocket_connection)



    async def handle_websocket_on_connected(self, *, websocket_connection):
        if websocket_connection.path == self.websocket_market_data_path:
            await self.websocket_market_data_subscribe(websocket_connection=websocket_connection)
        elif websocket_connection.path == self.websocket_account_path:
            await self.websocket_login(websocket_connection=websocket_connection)

    async def websocket_login(self, *, websocket_connection):
        await self.send_websocket_request(websocket_connection, websocket_request=self.websocket_login_create_websocket_request(time_point=time_point_now()))



    async def websocket_market_data_subscribe(self, *, websocket_connection):
        symbols_subsets = convert_set_to_subsets(input=self.symbols, subset_length=self.websocket_market_data_channel_symbols_limit)
        for symbols_subset in symbols_subsets:
            await self.send_websocket_request(websocket_connection, websocket_request=self.websocket_market_data_update_subscribe_create_websocket_request(symbols=symbols_subset, is_subscribe=True))
            await asyncio.sleep(self.websocket_market_data_channel_send_request_delay_seconds)

    async def websocket_account_subscribe(self, *, websocket_connection):
            await self.send_websocket_request(websocket_connection, websocket_request=self.websocket_account_update_subscribe_create_websocket_request(is_subscribe=True))

    async def websocket_on_disconnected(self,*,websocket_connection):
        logger.trace(f'base_url = {base_url}, path = {path}, query_params = {query_params}, websocket_connection = {websocket_connection}')
        await self.handle_websocket_on_disconnected(websocket_connection=websocket_connection)
        self._websocket_connections.pop((base_url,path, query_params), None)

    async def handle_websocket_on_disconnected(self, *, websocket_connection):
        pass

    async def websocket_on_message(self, *, base_url,path, query_params,websocket_connection, raw_websocket_message_data):
        websocket_message = WebsocketMessage(payload=raw_websocket_message_data, json_deserialize=self.json_deserialize)
        websocket_message = self.websocket_on_message_extract_data(websocket_message=websocket_message)
        websocket_request = None
        if websocket_message.websocket_request_id:
            websocket_request = self._websocket_requests.pop(websocket_message.websocket_request_id, None)
            websocket_message.websocket_request = websocket_request
        logger.trace(f'websocket_message = {self.json_serialize_pretty(websocket_message.as_json())}')
        json_deserialized_payload = websocket_message.json_deserialized_payload
        if self.is_websocket_push_data(base_url=base_url,path=path, query_params=query_params,websocket_message=websocket_message):
            if self.is_websocket_push_data_for_bbo(base_url=base_url,path=path, query_params=query_params,websocket_message=websocket_message):
                await self.handle_websocket_push_data_for_bbo(bbos=self.convert_websocket_response_for_bbo(json_deserialized_payload=json_deserialized_payload))
            elif self.is_websocket_push_data_for_trade(base_url=base_url,path=path, query_params=query_params,websocket_message=websocket_message):
                await self.handle_websocket_push_data_for_trade(trades=self.convert_websocket_response_for_trade(json_deserialized_payload=json_deserialized_payload))
            elif self.is_websocket_push_data_for_ohlcv(base_url=base_url,path=path, query_params=query_params,websocket_message=websocket_message):
                await self.handle_websocket_push_data_for_ohlcv(ohlcvs=self.convert_websocket_response_for_ohlcv(json_deserialized_payload=json_deserialized_payload))
        elif self.is_websocket_response_success(base_url=base_url,path=path, query_params=query_params,websocket_message=websocket_message):
            if self.is_websocket_response_for_create_order(base_url=base_url,path=path, query_params=query_params,websocket_message=websocket_message):
                await self.handle_websocket_response_for_create_order(order=self.convert_websocket_response_for_create_order(json_deserialized_payload=json_deserialized_payload,websocket_request=websocket_request))
            elif self.is_websocket_response_for_cancel_order(base_url=base_url,path=path, query_params=query_params,websocket_message=websocket_message):
                await self.handle_websocket_response_for_cancel_order(order=self.convert_websocket_response_for_cancel_order(json_deserialized_payload=json_deserialized_payload,websocket_request=websocket_request))
            elif self.is_websocket_response_for_subscribe(base_url=base_url,path=path, query_params=query_params,websocket_message=websocket_message):
                await self.handle_websocket_response_for_subscribe(base_url=base_url,path=path, query_params=query_params,websocket_message=websocket_message,websocket_connection=websocket_connection)
            elif self.is_websocket_response_for_login(base_url=base_url,path=path, query_params=query_params,websocket_message=websocket_message):
                await self.handle_websocket_response_for_login(base_url=base_url,path=path, query_params=query_params,websocket_message=websocket_message,websocket_connection=websocket_connection)
        else:
            await self.handle_websocket_response_for_error(base_url=base_url,path=path, query_params=query_params,websocket_message=websocket_message)


    def websocket_on_message_extract_data(self,*,websocket_message):
        raise NotImplementedError

    def is_websocket_push_data_for_bbo(self, *, json_deserialized_payload,payload_summary):
        return False

    def convert_websocket_response_for_bbo(self,*,json_deserialized_payload):
        raise NotImplementedError

    async def handle_websocket_push_data_for_bbo(self, *, bbos):
        logger.trace(f'bbos = {bbos}')
        for bbo in bbos:
            self._update_bbo(bbo=bbo)
        logger.trace(f'self.bbos = {self.bbos}')

    def is_websocket_push_data_for_trade(self, *, json_deserialized_payload,payload_summary):
        return False

    def convert_websocket_response_for_trade(self,*,json_deserialized_payload):
        raise NotImplementedError

    async def handle_websocket_push_data_for_trade(self, *, trades):
        logger.trace(f'trades = {trades}')
        if trades:
            symbol = trades[0].symbol
            trades_sorted = sorted(trades, key = lambda x: (x.exchange_update_time_point, x.trade_id))
            if symbol not in self.trades:
                self.trades[symbol] = trades_sorted
            else:
                tail = self.trades[symbol][-1]
                self.trades[symbol].extend([x for x in trades_sorted if (x.exchange_update_time_point, x.trade_id) > (tail.exchange_update_time_point, tail.trade_id)])
        logger.trace(f'self.trades = {self.trades}')


    def prune_trades(self):
        if self.keep_historical_trade_seconds is not None:
            for symbol, trades_for_symbol in self.trades.items():
                if trades_for_symbol:
                    head_exchange_update_time_point = trades_for_symbol[0].exchange_update_time_point[0]
                    earliest_exchange_update_time_point_to_keep = trades_for_symbol[-1].exchange_update_time_point[0] - self.keep_historical_trade_seconds
                    if head_exchange_update_time_point < earliest_exchange_update_time_point_to_keep:
                        self.trades[symbol] = [x for x in trades_for_symbol if x.exchange_update_time_point[0] >= earliest_exchange_update_time_point_to_keep]
        logger.trace(f'self.trades = {self.trades}')

    def prune_ohlcvs(self):
        if self.keep_historical_ohlcv_seconds is not None:
            for symbol, ohlcvs_for_symbol in self.ohlcvs.items():
                head_start_unix_timestamp_seconds = ohlcvs_for_symbol[0].start_unix_timestamp_seconds
                earliest_start_unix_timestamp_seconds_to_keep = ohlcvs_for_symbol[-1].start_unix_timestamp_seconds - self.keep_historical_ohlcv_seconds
                if head_start_unix_timestamp_seconds < earliest_start_unix_timestamp_seconds_to_keep:
                    self.ohlcvs[symbol] = [x for x in ohlcvs_for_symbol if x.start_unix_timestamp_seconds >= earliest_start_unix_timestamp_seconds_to_keep]
        logger.trace(f'self.ohlcvs = {self.ohlcvs}')

    def prune_orders(self):
        if self.keep_historical_order_seconds is not None:
            for symbol, orders_for_symbol in self.orders.items():
                latest_exchange_update_time_point = None
                for order in orders_for_symbol.values():
                    if order.is_closed and order.exchange_update_time_point is not None and (latest_exchange_update_time_point is None or order.exchange_update_time_point > latest_exchange_update_time_point):
                        latest_exchange_update_time_point = order.exchange_update_time_point
                if latest_exchange_update_time_point is not None:
                    earliest_exchange_update_time_point_to_keep = latest_exchange_update_time_point - self.keep_historical_order_seconds
                    self.orders[symbol] = { client_order_id: order for client_order_id, order in self.orders[symbol].items() if not order.is_closed or (order.exchange_update_time_point is not None and order.exchange_update_time_point >= earliest_exchange_update_time_point_to_keep)}


                if trades_for_symbol:
                    head_exchange_update_time_point = trades_for_symbol[0].exchange_update_time_point[0]
                    earliest_exchange_update_time_point_to_keep = trades_for_symbol[-1].exchange_update_time_point[0] - self.keep_historical_trade_seconds
                    if head_exchange_update_time_point < earliest_exchange_update_time_point_to_keep:
                        self.trades[symbol] = [x for x in trades_for_symbol if x.exchange_update_time_point[0] >= earliest_exchange_update_time_point_to_keep]
        logger.trace(f'self.trades = {self.trades}')

    def is_websocket_push_data_for_ohlcv(self, *, json_deserialized_payload,payload_summary):
        return False

    def convert_websocket_response_for_ohlcv(self,*,json_deserialized_payload):
        raise NotImplementedError

    async def handle_websocket_push_data_for_ohlcv(self, *, ohlcvs):
        logger.trace(f'ohlcvs = {ohlcvs}')
        if ohlcvs:
            symbol = ohlcvs[0].symbol
            ohlcvs_sorted = sorted(ohlcvs, key = lambda x: x.start_unix_timestamp_seconds)
            if symbol not in self.ohlcvs:
                self.ohlcvs[symbol] = ohlcvs_sorted
            else:
                tail = self.ohlcvs[symbol][-1]
                if tail.start_unix_timestamp_seconds == ohlcvs_sorted[0].start_unix_timestamp_seconds:
                    self.ohlcvs[symbol][-1] = ohlcvs_sorted[0]
                self.ohlcvs[symbol].extend([x for x in ohlcvs_sorted if (x.start_unix_timestamp_seconds) > (tail.start_unix_timestamp_seconds)])
        logger.trace(f'self.ohlcvs = {self.ohlcvs}')


    def is_websocket_response_success(self, *, json_deserialized_payload,payload_summary):
        return False

    def is_websocket_response_for_create_order(self, *, json_deserialized_payload,payload_summary):
        return False

    def is_websocket_response_for_cancel_order(self, *, json_deserialized_payload,payload_summary):
        return False

    def is_websocket_response_for_subscribe(self, *, json_deserialized_payload,payload_summary):
        return False

    def is_websocket_response_for_login(self, *, json_deserialized_payload,payload_summary):
        return False

    async def handle_websocket_response_for_subscribe(self, *,websocket_message,websocket_connection):
        logger.info(f'handle_websocket_response_for_subscribe: base_url = {base_url}, path = {path}, query_params = {query_params}, websocket_message = {self.json_serialize_pretty(websocket_message.as_json())}')
        self._websocket_reconnect_delay_seconds[websocket_connection.url_with_query_params] = 0

    async def handle_websocket_response_for_login(self, *,websocket_message,websocket_connection):
        logger.info(f'handle_websocket_response_for_login: base_url = {base_url}, path = {path}, query_params = {query_params}, websocket_message = {self.json_serialize_pretty(websocket_message.as_json())}')
        url_with_query_params = websocket_connection.url_with_query_params
        self._websocket_logged_in_connections.add(url_with_query_params)
        self._websocket_reconnect_delay_seconds[url_with_query_params] = 0
        if path == self.websocket_account_path:
            await self.websocket_account_subscribe(websocket_connection=websocket_connection)




    # def reset_websocket_reconnect_delay_seconds(self, *, url):
    #     self._websocket_reconnect_delay_seconds[url] = 1

    def get_websocket_reconnect_delay_seconds(self, *, websocket_connection):
        url_with_query_params = websocket_connection.url_with_query_params
        if url_with_query_params not in self._websocket_reconnect_delay_seconds:
            self._websocket_reconnect_delay_seconds[url_with_query_params] = 1
        else:
            self._websocket_reconnect_delay_seconds[url_with_query_params] = min(self._websocket_reconnect_delay_seconds[url_with_query_params]*2, 60)
        return self._websocket_reconnect_delay_seconds[url_with_query_params]

    async def send_websocket_request(self,*,websocket_connection, websocket_request):
        logger.trace(f'websocket_request = {websocket_request}')
        if websocket_request.payload:
            await websocket_connection.connection.send_str(websocket_request.payload)

    def create_nextrest_request_id(self):
        self._next_rest_request_id_int += 1
        return str(self._next_rest_request_id_int)

    def create_nextwebsocket_request_id(self):
        self._next_websocket_request_id_int += 1
        return str(self._next_websocket_request_id_int)

    def create_nextclient_order_id(self):
        self._next_client_order_id_int += 1
        return str(self._next_client_order_id_int)

    def rest_create_get_request_function(self, **kwargs):
        def rest_request_function(*, time_point):
            rest_request = RestRequest(id=self.create_next_rest_request_id(), base_url=self.rest_base_url, method=RestRequest.METHOD_GET, **kwargs)
            return rest_request
        return rest_request_function

    def rest_create_get_request_function_with_signature(self, **kwargs):
        return self.rest_create_request_function_with_signature(method=RestRequest.METHOD_GET, **kwargs)

    def rest_create_post_request_function_with_signature(self, **kwargs):
        return self.rest_create_request_function_with_signature(method=RestRequest.METHOD_POST, **kwargs)

    def rest_create_delete_request_function_with_signature(self, **kwargs):
        return self.rest_create_request_function_with_signature(method=RestRequest.METHOD_DELETE, **kwargs)

    def rest_create_request_function_with_signature(self, *, method, **kwargs):
        def rest_request_function(*, time_point):
            rest_request = RestRequest(id=self.create_next_rest_request_id(), base_url=self.rest_base_url, method=method, **kwargs)
            self.sign_request(rest_request=rest_request, time_point=time_point)
            return rest_request
        return rest_request_function

    def sign_request(self, *, rest_request, time_point):
        raise NotImplementedError

    def is_rest_response_success(self,*,rest_response):
        return rest_response.status_code >= 200 and rest_response.status_code < 300

    def is_rest_response_for_all_instrument_information(self,*,rest_response):
        return False

    def is_rest_response_for_bbo(self,*,rest_response):
        return False

    def is_rest_response_for_historical_trade(self,*,rest_response):
        return False

    def is_rest_response_for_historical_ohlcv(self,*,rest_response):
        return False

    def is_rest_response_for_create_order(self,*,rest_response):
        return False

    def is_rest_response_for_cancel_order(self,*,rest_response):
        return False

    def is_rest_response_for_fetch_order(self,*,rest_response):
        return False

    def is_rest_response_for_fetch_open_order(self,*,rest_response):
        return False

    def convert_rest_response_for_all_instrument_information(self,*,json_deserialized_payload,rest_request):
        raise NotImplementedError

    def convert_rest_response_for_bbo(self,*,json_deserialized_payload,rest_request):
        raise NotImplementedError

    def convert_rest_response_for_historical_trade(self,*,json_deserialized_payload,rest_request):
        raise NotImplementedError

    def convert_rest_response_for_historical_trade_to_next_rest_request_function(self,*,json_deserialized_payload,rest_request):
        raise NotImplementedError

    def convert_rest_response_for_historical_ohlcv(self,*,json_deserialized_payload,rest_request):
        raise NotImplementedError

    def convert_rest_response_for_historical_ohlcv_to_next_rest_request_function(self,*,json_deserialized_payload,rest_request):
        raise NotImplementedError

    def convert_rest_response_for_create_order(self,*,json_deserialized_payload,rest_request):
        raise NotImplementedError

    def convert_rest_response_for_cancel_order(self,*,json_deserialized_payload,rest_request):
        raise NotImplementedError

    def convert_rest_response_for_fetch_order(self,*,json_deserialized_payload,rest_request):
        raise NotImplementedError

    def convert_rest_response_for_fetch_open_order(self,*,json_deserialized_payload,rest_request):
        raise NotImplementedError

    def convert_rest_response_for_fetch_open_order_to_next_rest_request_function(self,*,json_deserialized_payload,rest_request):
        raise NotImplementedError


    async def handle_rest_response_for_all_instrument_information(self,*,all_instrument_information):
        logger.trace(f'all_instrument_information = {all_instrument_information}')
        for instrument_information in all_instrument_information:
            self.all_instrument_information[instrument_information.symbol] = instrument_information
        # todo: remove delisted instruments
        logger.trace(f'self.all_instrument_information = {self.all_instrument_information}')

    async def handle_rest_response_for_bbo(self,*,bbos):
        logger.trace(f'bbos = {bbos}')
        for bbo in bbos:
            self._update_bbo(bbo=bbo)
        logger.trace(f'self.bbos = {self.bbos}')

    async def handle_rest_response_for_historical_trade(self,*,historical_trades):
        logger.trace(f'historical_trades = {historical_trades}')
        if historical_trades:
            symbol = historical_trades[0].symbol
            historical_trades_filtered = [x for x in historical_trades if (self.fetch_historical_trade_start_unix_timestamp_seconds is None or x.exchange_update_time_point[0] >= self.fetch_historical_trade_start_unix_timestamp_seconds) and (self.fetch_historical_trade_end_unix_timestamp_seconds is None or x.exchange_update_time_point[0] < self.fetch_historical_trade_end_unix_timestamp_seconds)]
            historical_trades_sorted = sorted(historical_trades_filtered, key = lambda x: (x.exchange_update_time_point, x.trade_id), reverse=True)
            if symbol not in self.trades:
                self.trades[symbol] = list(reversed(historical_trades_sorted))
            else:
                head = self.trades[symbol][0]
                self.trades[symbol][:0] = list(reversed([x for x in historical_trades_sorted if (x.exchange_update_time_point, x.trade_id) < (head.exchange_update_time_point, head.trade_id)]))
        logger.trace(f'self.trades = {self.trades}')


    async def handle_rest_response_for_historical_ohlcv(self,*,historical_ohlcvs):
        logger.trace(f'historical_ohlcvs = {historical_ohlcvs}')
        if historical_ohlcvs:
            symbol = historical_ohlcvs[0].symbol
            historical_ohlcvs_filtered = [x for x in historical_ohlcvs if (self.fetch_historical_ohlcv_start_unix_timestamp_seconds is None or x.start_unix_timestamp_seconds >= self.fetch_historical_ohlcv_start_unix_timestamp_seconds) and (self.fetch_historical_ohlcv_end_unix_timestamp_seconds is None or x.start_unix_timestamp_seconds < self.fetch_historical_ohlcv_end_unix_timestamp_seconds)]
            historical_ohlcvs_sorted = sorted(historical_ohlcvs_filtered, key = lambda x: x.start_unix_timestamp_seconds, reverse=True)
            if symbol not in self.ohlcvs:
                self.ohlcvs[symbol] = list(reversed(historical_ohlcvs_sorted))
            else:
                head = self.ohlcvs[symbol][0]
                self.ohlcvs[symbol][:0] = list(reversed([x for x in historical_ohlcvs_sorted if x.start_unix_timestamp_seconds < head.start_unix_timestamp_seconds]))
        logger.trace(f'self.ohlcvs = {self.ohlcvs}')

    async def handle_rest_response_for_create_order(self,*,order):
        logger.trace(f'order = {order}')
        self._update_order(order=order)

    async def handle_rest_response_for_cancel_order(self,*,order):
        logger.trace(f'order = {order}')
        self._update_order(order=order)

    async def handle_rest_response_for_fetch_order(self,*,order):
        logger.trace(f'order = {order}')
        self._update_order(order=order)

    async def handle_rest_response_for_fetch_open_order(self,*,open_orders):
        logger.trace(f'open_orders = {open_orders}')
        for open_order in open_orders:
            self._update_order(order=open_order)

    async def handle_rest_response_for_error(self,*,rest_response):
        raise NotImplementedError




    def websocket_market_data_update_subscribe_create_websocket_request(self, *,symbols, is_subscribe):
        raise NotImplementedError

    def websocket_login_create_websocket_request(self, *, time_point):
        raise NotImplementedError

    def websocket_account_update_subscribe_create_websocket_request(self, *, is_subscribe):
        raise NotImplementedError

    def convert_ohlcv_interval_seconds_to_string(self, *, ohlcv_interval_seconds):
        raise NotImplementedError

    def websocket_create_request(self, **kwargs):
        websocket_request = WebsocketRequest(id=self.create_next_websocket_request_id(), base_url=self.websocket_base_url, **kwargs)
        return websocket_request

    def _update_bbo(self, *, bbo):
        if bbo.symbol not in self.bbos or self.bbos[bbo.symbol].exchange_update_time_point < bbo.exchange_update_time_point:
            self.bbos[bbo.symbol] = bbo

    def _update_order(self, *, order):
        order_to_update = self._get_order(symbol=order.symbol, client_order_id=order.client_order_id)
        logger.trace(f'order_to_update = {order_to_update}')
        if order_to_update:
            exchange_update_time_point = order_to_update.exchange_update_time_point
            status = order_to_update.status
            cumulative_filled_quantity = order_to_update.cumulative_filled_quantity

            has_fill = order.cumulative_filled_quantity is not None and (cumulative_filled_quantity is None or order.cumulative_filled_quantity_as_decimal > Decimal(cumulative_filled_quantity))

            # print((order.exchange_update_time_point is not None and (exchange_update_time_point is None or order.exchange_update_time_point > exchange_update_time_point)) or (order.status is not None and (status is None or order.status > status)) or has_fill)

            if (order.exchange_update_time_point is not None and (exchange_update_time_point is None or order.exchange_update_time_point > exchange_update_time_point)) or (order.status is not None and (status is None or order.status > status)) or has_fill:
                api_method = order_to_update.api_method
                symbol = order_to_update.symbol
                exchange_update_time_point = order.exchange_update_time_point
                order_id = order_to_update.order_id
                if order.order_id is not None and order.order_id != order_id:
                    order_id = order.order_id
                order_id = order_to_update.order_id
                client_order_id = order_to_update.client_order_id
                is_buy = order_to_update.is_buy
                limit_price = order_to_update.limit_price

                # because for some exchange, self trade prevention might change the order's quantity
                quantity = order_to_update.quantity
                if order.quantity is not None and order.quantity != quantity:
                    quantity = order.quantity

                is_post_only = order_to_update.is_post_only
                is_fok = order_to_update.is_fok
                is_ioc = order_to_update.is_ioc
                is_reduce_only = order_to_update.is_reduce_only

                cumulative_filled_quantity = order_to_update.cumulative_filled_quantity
                cumulative_filled_quote_quantity = order_to_update.cumulative_filled_quote_quantity
                if has_fill:
                    cumulative_filled_quantity = order.cumulative_filled_quantity
                    cumulative_filled_quote_quantity = order.cumulative_filled_quote_quantity

                exchange_create_time_point = order_to_update.exchange_create_time_point
                if exchange_create_time_point is None and order.exchange_create_time_point is not None:
                    exchange_create_time_point = order.exchange_create_time_point

                status = order.status

                self._upsert_order(order=Order(
                    api_method = api_method,
                    symbol=symbol,
                    exchange_update_time_point=exchange_update_time_point,
                    order_id=order_id,
                    client_order_id=client_order_id,
                    is_buy=is_buy,
                    limit_price=limit_price,
                    quantity=quantity,
                    is_post_only=is_post_only,
                    is_fok=is_fok,
                    is_ioc=is_ioc,
                    is_reduce_only=is_reduce_only,
                    cumulative_filled_quantity=cumulative_filled_quantity,
                    cumulative_filled_quote_quantity=cumulative_filled_quote_quantity,
                    exchange_create_time_point=exchange_create_time_point,
                    status=status,
                ))
        else:
            self._upsert_order(order=order)
        logger.trace(f'updated order = {self.orders[order.symbol][order.client_order_id]}')

    def _get_order(self, *, symbol, client_order_id):
        return self.orders.get(symbol, {}).get(client_order_id)

    def _has_order(self, *, symbol, client_order_id):
        return symbol in self.orders and client_order_id in self.orders[symbol]

    def _upsert_order(self,*,order):
        logger.trace(f'order = {order}')
        if order.symbol not in self.orders:
            self.orders[order.symbol] = {}
        self.orders[order.symbol][order.client_order_id] = order
    # def _delete_order(self, *, symbol, client_order_id):
    #     if symbol in self.orders:
    #         self.orders[symbol].pop(client_order_id, None)

    def _replace_order(self,*,symbol,client_order_id, **kwargs):
        print(f'self.orders = {self.orders}')
        if self._has_order(symbol=symbol,client_order_id=client_order_id):
            self.orders[symbol][client_order_id] = dataclasses.replace(self.orders[symbol][client_order_id], **kwargs)

    def _extract_order_from_dict(self,*,input):
        raise NotImplementedError
