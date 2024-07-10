import modbus_tcp

class ModbusTCPClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = modbus_tcp.ModbusTCPClient(self.host, self.port)

    def connect(self):
        self.client.connect()

    def read_holding_registers(self, address, count):
        return self.client.read_holding_registers(address, count)

    def write_single_register(self, address, value):
        self.client.write_single_register(address, value)
