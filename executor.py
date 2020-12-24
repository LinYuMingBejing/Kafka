import argparse
from consumer import Consumer
from datetime import datetime
import json


ap = argparse.ArgumentParser()
ap.add_argument("-topic", dest="topic", required=True,
                help="choose kafka topic: Required")
ap.add_argument("-group_id", dest="group_id", required=True,
                help="choose kafka group_id: Required")
ap.add_argument("-ip", dest="ip", required=True,
                help="insert ip location: Required(ex: 127.0.0.1)")
args = ap.parse_args()


def output(data):
    print(data)


if __name__ == '__main__':
    now = datetime.now()
    message = {'level': 'INFO', 'message': 'Start consume. topic:{}, group_id:{}. kafka_ip:{}'\
        .format(args.topic, args.group_id, args.ip), 'datetime': now.strftime('%Y-%m-%d %H:%M:%S')}
    print(json.dumps(message), flush=True)
    while True:
        Consumer(args.topic, args.group_id, [args.ip]).consume(output)