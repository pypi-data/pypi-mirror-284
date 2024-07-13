class RestResponse:

    def __init__(self, *, status_code=None, payload=None, headers=None,json_deserialize=None, rest_request=None,  next_rest_request_function=None, next_rest_request_delay_seconds=0):
        self.status_code = status_code
        self.payload = payload
        self.headers = headers
        self.json_deserialized_payload = json_deserialize(payload) if payload and headers["Content-Type"].startswith('application/json') and json_deserialize else None
        self.rest_request = rest_request
        self.create_next_rest_request_function = next_rest_request_function
        self.create_next_rest_request_delay_seconds = next_rest_request_delay_seconds

    def as_json(self):
        return {
            'status_code':self.status_code,
            'payload':self.payload,
            'headers':dict(self.headers),
            'json_deserialized_payload':self.json_deserialized_payload,
            'rest_request':self.rest_request.as_json(),
            'has_next_rest_request_function':self.create_next_rest_request_function is not None,
            'next_rest_request_delay_seconds':self.create_next_rest_request_delay_seconds,
        }

    def __repr__(self):
        return f'{self.__dict__}'
