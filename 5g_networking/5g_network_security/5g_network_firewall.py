import socket

class FiveGNetworkFirewall:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def block_traffic(self, src_ip, dst_ip, src_port, dst_port):
        self.socket.bind((src_ip, src_port))
        self.socket.connect((dst_ip, dst_port))
        self.socket.close()

    def allow_traffic(self, src_ip, dst_ip, src_port, dst_port):
        self.socket.bind((src_ip, src_port))
        self.socket.listen(1)
        conn, addr = self.socket.accept()
        conn.close()
