from crypto_chassis_trade.helper import create_url_with_query_params

class WebsocketConnection:

    def __init__(self, *, base_url= None, path= None, query_params=None, connection=None):
        self.base_url = base_url
        self.path = path
        self.query_params=query_params
        self.connection = connection

    def as_json(self):
        return {
            'base_url':self.base_url,
            'path':self.path,
            'query_params':query_params,
        }

    def __repr__(self):
        return f'{self.__dict__}'

    @property
    def url_with_query_params(self):
        return create_url_with_query_params(base_url=self.base_url, path=self.path, query_params=self.query_params)
