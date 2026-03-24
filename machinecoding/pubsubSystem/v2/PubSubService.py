from concurrent.futures import ThreadPoolExecutor
import threading
from entities.Topic import Topic
from typing import Dict
class PubSubService:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is  None:
                    cls._instance = super().__new__(cls)
                    cls.initialize = False
        return cls._instance
    
    def __init__(self):
        if self.initialize:
            return
        self.initialize = True
        self.executor = ThreadPoolExecutor()
        self.map:Dict[str, Topic] = {}

    @classmethod
    def get_instance(cls):
        return cls()
    
    def create_topic(self, tpc_nm):
        self.map[tpc_nm]  = Topic(tpc_nm, self.executor)
        return
    def subscribe(self, tpc_nm, subscriber):
        tpc = self.map.get(tpc_nm)
        if not tpc:
            print("Topic not found")
        tpc.add_subscriber(subscriber)

    def unsubscribe(self, tpc_nm, subscriber):
        tpc = self.map.get(tpc_nm)
        if not tpc:
            print("Topic not found")
        tpc.remove_subscriber(subscriber)
    
    def publish(self,tpc_nm, message):
        tpc = self.map.get(tpc_nm)
        if not tpc:
            print("Topic not found")
        tpc.broadcast(message)
    def shutdown(self):
        self.executor.shutdown(wait=True)