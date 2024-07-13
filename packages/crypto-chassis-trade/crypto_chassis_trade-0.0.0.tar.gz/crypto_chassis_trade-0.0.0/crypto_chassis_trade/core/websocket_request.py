from crypto_chassis_trade.helper import create_url


class WebsocketRequest:

    def __init__(self, *, id= None,base_url= None, path= None, query_params=None, payload = None, json_payload = None, json_serialize=None, extra_data=None):
        self.id = id
        self.base_url = base_url
        self.path = path
        self.query_params = query_params
        self.json_payload = json_payload
        if json_payload and json_serialize:
            self.payload = json_serialize(json_payload)
        else:
            self.payload = payload
        self.extra_data = extra_data

    def as_json(self):
        return self.__dict__

    def __repr__(self):
        return f'{self.__dict__}'

    @property
    def url(self):
        return create_url(base_url=self.base_url, path=self.path)
