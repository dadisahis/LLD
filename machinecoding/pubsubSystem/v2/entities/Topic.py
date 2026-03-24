class Topic:
    def __init__(self, name, executor):
        self.name = name
        self.executor = executor
        self.subscribers = set()
    def add_subscriber(self, subscriber):
        self.subscribers.add(subscriber)
    def remove_subscriber(self, subscriber):
        self.subscribers.remove(subscriber)

    def broadcast(self, message):
        for sb in self.subscribers:
            self.executor.submit(self._deliver, sb, message)

    def _deliver(self, subcriber, message):
        try:
            subcriber.on_message(message)
        except Exception as e:
            print(str(e))
            raise Exception("Error incurred")