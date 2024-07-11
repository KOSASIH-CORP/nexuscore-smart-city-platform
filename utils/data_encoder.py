import json

class DataEncoder:
    def __init__(self):
        pass

    def encode(self, data):
        return json.dumps(data)

    def decode(self, encoded_data):
        return json.loads(encoded_data)
