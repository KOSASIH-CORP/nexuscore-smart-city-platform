import asyncio
import json
from aiohttp import ClientSession
import tensorflow as tf

class EdgeDevice:
    def __init__(self, device_id, device_type):
        self.device_id = device_id
        self.device_type = device_type
        self.session = ClientSession()
        self.model = tf.keras.models.load_model("edge_model.h5")

    async def process_data(self, data):
        # Preprocess data
        data = tf.convert_to_tensor(data, dtype=tf.float32)
        data = tf.reshape(data, (-1, 10, 10))

        # Run inference on the edge model
        output = self.model.predict(data)

        # Postprocess output
        output = tf.argmax(output, axis=1)

        return output.numpy()

    async def send_data(self, data):
        async with self.session.post(f"http://localhost:8080/api/devices/{self.device_id}/data", json=data) as response:
            return await response.json()

async def main():
    device = EdgeDevice("edge_device", "edge")
    while True:
        data = await device.receive_data()
        output = await device.process_data(data)
        await device.send_data(output)
        await asyncio.sleep(1)

asyncio.run(main())
