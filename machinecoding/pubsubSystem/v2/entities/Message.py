from datetime import datetime
class Message:
    def __init__(self, payload):
        self._payload = payload
        self._ts = datetime.now()

    def get_payload(self):
        return self._payload
    
    def get_ts(self):
        return self._ts
    

