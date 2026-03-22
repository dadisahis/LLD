from datetime import datetime
class Message:
    def __init__(self, payload):
        self._payload = payload
        self._ts = datetime.now()

    def get_payload(self):
        return self._payload
    
    def __str__(self):
        print(f"Message{{payload='{self._payload}'}}")
        