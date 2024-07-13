class WebsocketMessage:

    def __init__(self, *, payload=None, json_deserialize=None, payload_summary=None, websocket_request_id = None, websocket_request = None):
        self.payload = payload
        self.json_deserialized_payload = json_deserialize(payload) if payload and json_deserialize else None
        # arbitrary dict containing parsed information (very specific for each exchange)
        self.payload_summary=payload_summary
        self.websocket_request_id = websocket_request_id
        self.websocket_request = websocket_request

    def as_json(self):
        return {
            'payload':self.payload,
            'json_deserialized_payload':self.json_deserialized_payload,
            'payload_summary':self.payload_summary,
            'websocket_request_id':self.websocket_request_id,
            'websocket_request':self.websocket_request.as_json(),
        }

    def __repr__(self):
        return f'{self.__dict__}'
