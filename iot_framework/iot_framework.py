import asyncio
import json
from aiohttp import ClientSession

class IoTDevice:
    def __init__(self, device_id, device_type):
        self.device_id = device_id
        self.device_type = device_type

    async def send_data(self, data):
        async with ClientSession() as session:
            async with session.post(f"http://localhost:8080/api/devices/{self.device_id}/data", json=data) as response:
                return await response.json()

class IoTGateway:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    async def process_data(self):
        for device in self.devices:
            data = await device.send_data({"temperature": 25, "humidity": 60})
            print(f"Received data from {device.device_id}: {data}")

async def main():
    gateway = IoTGateway()
    device1 = IoTDevice("device1", "temperature_sensor")
    device2 = IoTDevice("device2", "humidity_sensor")
    gateway.add_device(device1)
    gateway.add_device(device2)
    await gateway.process_data()

asyncio.run(main())
