from crypto_chassis_trade.helper import create_url, create_path_with_query_params


class RestRequest:
    METHOD_GET = 'GET'
    METHOD_HEAD = 'HEAD'
    METHOD_POST = 'POST'
    METHOD_PUT = 'PUT'
    METHOD_DELETE = 'DELETE'
    METHOD_CONNECT = 'CONNECT'
    METHOD_OPTIONS = 'OPTIONS'
    METHOD_TRACE = 'TRACE'
    METHOD_PATCH = 'PATCH'

    def __init__(self, *, id= None, base_url= None, method= None, path= None, query_params= None, payload= None, headers= None, json_payload=None, json_serialize=None, extra_data=None):
        self.id = id
        self.base_url = base_url
        self.method = method
        self.path = path
        self.query_params = query_params
        self.headers = headers
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

    @property
    def path_with_query_params(self):
        return create_path_with_query_params(path=self.path,query_params=self.query_params)
