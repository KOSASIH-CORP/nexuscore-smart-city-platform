import socket

class BMSGateway:
    def __init__(self, bms_ip, bms_port):
        self.bms_ip = bms_ip
        self.bms_port = bms_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_bms(self):
        self.socket.connect((self.bms_ip, self.bms_port))

    def send_command(self, command):
        self.socket.send(command.encode())

    def receive_data(self):
        data = self.socket.recv(1024)
        return data.decode()

    def disconnect_from_bms(self):
        self.socket.close()
