import paho.mqtt.client as mqtt

class IIoTDeviceManagementMQTT:
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

    def device_registration(self, device_id, device_type):
        payload = {'device_id': device_id, 'device_type': device_type}
        self.publish('device/registration', json.dumps(payload))

    def device_status_update(self, device_id, status):
        payload = {'device_id': device_id, 'status': status}
        self.publish('device/status', json.dumps(payload))
