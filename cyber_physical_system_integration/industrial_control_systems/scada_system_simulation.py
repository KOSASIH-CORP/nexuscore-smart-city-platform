import random

class SCADASystemSimulation:
    def __init__(self, num_devices):
        self.num_devices = num_devices
        self.devices = []
        for i in range(num_devices):
            self.devices.append({'id': i, 'status': 'online', 'data': []})

    def simulate_data(self):
        for device in self.devices:
            device['data'].append(random.uniform(0, 100))

    def get_device_data(self, device_id):
        return self.devices[device_id]['data']

    def set_device_status(self, device_id, status):
        self.devices[device_id]['status'] = status

    def get_device_status(self, device_id):
        return self.devices[device_id]['status']
