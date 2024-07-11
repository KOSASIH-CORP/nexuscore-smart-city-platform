import socket

class NodeCommunication:
    def __init__(self, node_id, node_address, node_port):
        self.node_id = node_id
        self.node_address = node_address
        self.node_port = node_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_node(self):
        self.socket.connect((self.node_address, self.node_port))

    def send_data(self, data):
        self.socket.send(data.encode())

    def receive_data(self):
        return self.socket.recv(1024).decode()

    def close_connection(self):
        self.socket.close()
