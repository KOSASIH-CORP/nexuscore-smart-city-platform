import serial

class DeviceDriver:
    def __init__(self, device_port):
        self.device_port = device_port
        self.ser = serial.Serial(device_port, 9600, timeout=1)

    def read_data(self):
        return self.ser.readline().decode()

    def write_data(self, data):
        self.ser.write(data.encode())
