from kafka import KafkaConsumer
import json
import traceback


class Consumer:

    __consumer = None
    enable_auto_commit = True
    auto_commit_interval_ms = 500


    def __init__(self, topic, group_id, bootstrap_servers):
        self.topic = topic
        self.group_id = group_id
        self.bootstrap_servers = bootstrap_servers


    def consumer(self):
        return KafkaConsumer(
                self.topic,
                group_id = self.group_id,
                bootstrap_servers = self.bootstrap_servers,
                enable_auto_commit = self.enable_auto_commit,
                auto_commit_interval_ms = self.auto_commit_interval_ms,
                value_deserializer=lambda m: json.loads(m.decode('ascii'))
            )
    

    def consume(self, func):
        if not self.__consumer:
            self.__consumer = self.consumer()
        
        for message in self.__consumer:
            try:
                func(message.value)
            except Exception as e:
                message = {'level': 'ERROR', 'message': traceback.format_exc(), 'value': message.value}
                print(json.dumps(message), flush=True)
                continue