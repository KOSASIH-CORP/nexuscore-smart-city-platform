import opcua

class CyberPhysicalSystemIntegration:
    def __init__(self, opcua_server_url):
        self.opcua_server_url = opcua_server_url
        self.client = opcua.Client(self.opcua_server_url)

    def connect(self):
        self.client.connect()

    def read_data(self, node_id):
        node = self.client.get_node(node_id)
        return node.get_value()

    def write_data(self, node_id, value):
        node = self.client.get_node(node_id)
        node.set_value(value)
