import socket
import json

class DeviceCommunication:
    def __init__(self, device_ip, device_port):
        self.device_ip = device_ip
        self.device_port = device_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((device_ip, device_port))
    
    def send_command(self, command):
        # Send command to device using JSON protocol
        data = json.dumps({'command': command})
        self.socket.send(data.encode())
    
    def receive_data(self):
        # Receive data from device using JSON protocol
        data = self.socket.recv(1024)
        data = json.loads(data.decode())
        return data
    
    def close_connection(self):
        # Close connection to device
        self.socket.close()
