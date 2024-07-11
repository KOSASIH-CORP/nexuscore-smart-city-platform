import modbus

class SCADASystem:
    def __init__(self, modbus_tcp_ip, modbus_tcp_port):
        self.modbus_tcp_ip = modbus_tcp_ip
        self.modbus_tcp_port = modbus_tcp_port
        self.modbus_client = modbus.ModbusTcpClient(self.modbus_tcp_ip, self.modbus_tcp_port)

    def connect_to_scada(self):
        self.modbus_client.connect()

    def read_data_from_scada(self, register_address, num_registers):
        return self.modbus_client.read_holding_registers(register_address, num_registers)

    def write_data_to_scada(self, register_address, values):
        self.modbus_client.write_multiple_registers(register_address, values)

    def disconnect_from_scada(self):
        self.modbus_client.close()
