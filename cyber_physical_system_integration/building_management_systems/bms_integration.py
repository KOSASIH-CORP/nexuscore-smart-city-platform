import bacnet

class BMSIntegration:
    def __init__(self, bms_ip_address, bms_port):
        self.bms_ip_address = bms_ip_address
        self.bms_port = bms_port
        self.client = bacnet.BACnetClient(self.bms_ip_address, self.bms_port)

    def connect(self):
        self.client.connect()

    def read_data(self, object_id):
        return self.client.read_property(object_id, 'presentValue')

    def write_data(self, object_id, value):
        self.client.write_property(object_id, 'presentValue', value)
