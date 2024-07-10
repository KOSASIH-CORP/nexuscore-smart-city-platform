import paho.mqtt.client as mqtt

class IIoTGateway:
    def __init__(self, broker_url, broker_port):
        self.broker_url = broker_url
        self.broker_port = broker_port
        self.client = mqtt.Client()

    def connect(self):
        self.client.connect(self.broker_url, self.broker_port)

    def publish(self, topic, payload):
        self.client.publish(topic, payload)

    def subscribe(self, topic):
        self.client.subscribe(topic)
