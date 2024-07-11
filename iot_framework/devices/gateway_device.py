import asyncio
import json
from aiohttp import ClientSession

class GatewayDevice:
    def __init__(self, device_id, device_type):
        self.device_id = device_id
        self.device_type = device_type
        self.session = ClientSession()

    async def send_data(self, data):
        async with self.session.post(f"http://localhost:8080/api/devices/{self.device_id}/data", json=data) as response:
            return await response.json()

    async def receive_command(self):
        async with self.session.get(f"http://localhost:8080/api/devices/{self.device_id}/commands") as response:
            return await response.json()

    async def process_command(self, command):
        # Implement command processing logic
        print(f"Received command: {command}")

async def main():
    device = GatewayDevice("gateway_device", "gateway")
    while True:
        command = await device.receive_command()
        await device.process_command(command)
        await asyncio.sleep(1)

asyncio.run(main())
