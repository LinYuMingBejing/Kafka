from kafka import KafkaProducer
from kafka.errors import KafkaError
import json


class Producer:
    
    __producer = None

    def __init__(self, topic, bootstrap_servers, linger_ms, batch_size):
        self.topic = topic
        self.bootstrap_servers = bootstrap_servers
        self.linger_ms = linger_ms
        self.batch_size = batch_size
    

    def producer(self):
        return KafkaProducer(
            bootstrap_servers = self.bootstrap_servers,
            linger_ms = self.linger_ms,
            batch_size = self.batch_size,
            value_serializer = lambda m: json.dumps(m).encode('ascii')
        )
    

    def send_message(self, message):
        if not self.__producer:
            self.__producer = self.producer()

        self.__producer.send(self.topic, value = message)

    
    def close(self):
        self.__producer.flush()
        self.__producer.close()