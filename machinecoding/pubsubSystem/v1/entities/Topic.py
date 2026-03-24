from .SubscrberStrategy import *
class Topic:
    def __init__(self, name, deliveryExecutor):
        self.name = name
        self.deliveryExecutor = deliveryExecutor
        self.subscibers = set()
    
    def get_name(self):
        return self.name
    def add_subscriber(self, subscriber: 'Subcsriber'):
        self.subscibers.add(subscriber)

    def remove_subscriber(self, subscriber: 'Subcsriber'):
        self.subscibers.remove(subscriber)

    def broadcast(self, message):
        for subsc in self.subscibers:
            self.deliveryExecutor.submit(self._deliver_message, subsc, message)
        
    def _deliver_message(self, subscriber: 'Subcsriber', message: Message):
        try:
            subscriber.onMessage(message)
        except Exception as e:
            print(f"Delivery Failed to subscriber: {subscriber.get_id()} : {str(e)}")
        