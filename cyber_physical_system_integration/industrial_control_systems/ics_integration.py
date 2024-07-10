import pyModbusTCP

class ICSIntegration:
    def __init__(self, modbus_tcp_server):
        self.modbus_tcp_server = modbus_tcp_server
        self.client = pyModbusTCP.ModbusTcpClient(self.modbus_tcp_server)

    def connect(self):
        self.client.connect()

    def read_data(self, register_address):
        return self.client.read_holding_registers(register_address, 1)[0]

    def write_data(self, register_address, value):
        self.client.write_single_register(register_address, value)
