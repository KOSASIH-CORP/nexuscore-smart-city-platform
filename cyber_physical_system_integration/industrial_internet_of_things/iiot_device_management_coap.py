import coapthon

class IIoTDeviceManagementCoAP:
    def __init__(self, server_url):
        self.server_url = server_url
        self.client = coapthon.CLI(self.server_url)

    def discover_devices(self):
        response = self.client.discover()
        return response

    def register_device(self, device_id, device_type):
        payload = {'device_id': device_id, 'device_type': device_type}
        response = self.client.post('device/registration', payload)
        return response

    def update_device_status(self, device_id, status):
        payload = {'device_id': device_id, 'tatus': status}
        response = self.client.put('device/status', payload)
        return response
