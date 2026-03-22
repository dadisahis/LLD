from concurrent.futures import ThreadPoolExecutor
import threading
from entities.Topic import Topic
class PubSubService:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.initialize = False

        return cls._instance
    
    def __init__(self):
        if self.initialize:
            return
        self.topicRegister = {}
        self.deliveryExecutor = ThreadPoolExecutor()
        self.initialize = True


    @classmethod
    def get_instance(cls):
        return cls()
    

    def create_topic(self, topic_name):
        if topic_name not in self.topicRegister:
            self.topicRegister[topic_name] = Topic(topic_name, self.deliveryExecutor)
        print("Topic name created")
    def subscribe(self, topic_name, subcriber):
        topic = self.topicRegister.get(topic_name)
        if topic is None:
            raise ValueError("Topic doesnt exists")
        topic.add_subscriber(subcriber)
        print(f"Subscriber: {subcriber.get_id()} subscribed to {topic_name}")
    
    def unsubscribe(self, topic_name, subcriber):
        topic = self.topicRegister.get(topic_name)
        if topic is None:
            raise ValueError("Topic doesnt exists")
        topic.remove_subscriber(subcriber)
        print(f"Subscriber: {subcriber.get_id()} unsubscribed to {topic_name}")

    def publish(self, topic_name, message):
        topic = self.topicRegister.get(topic_name)
        if topic is None:
            raise ValueError("Topic doesnt exists")
        topic.broadcast(message)

    def shutdown(self):
        print("Pub Sub Shutting down")
        self.deliveryExecutor.shutdown()
        print("Pub Sub Shut down complete")        