from interfaces import *
 
class Subscriber(ISubscriber):   
    def __init__(self, name: str):
        self.name = name
        
    def update(self, message: str):
        print(f"{self.name} received a message: {message}")
    
    def __eq__(self, other: object):
        if isinstance(other, Subscriber):
            return self.name == other.name
        
        return False


class Publisher(IPublisher[Subscriber]):    
    def __init__(self):
        self.subscribers: list[Subscriber] = []
        
    def add_subscriber(self, subscriber: Subscriber):
        self.subscribers.append(subscriber)
        
    def remove_subscriber(self, subscriber: Subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)
        
    def notify_subscribers(self, message: str):
        for subscriber in self.subscribers:
            subscriber.update(message)


if __name__ == "__main__":
    publisher = Publisher()
    subscriber1 = Subscriber("Subscriber1")
    subscriber2 = Subscriber("Subscriber2")

    publisher.add_subscriber(subscriber1)
    publisher.add_subscriber(subscriber2)

    publisher.notify_subscribers("Hello, subscribers!")
    publisher.remove_subscriber(subscriber1)

    publisher.notify_subscribers("Observer pattern is cool!")
