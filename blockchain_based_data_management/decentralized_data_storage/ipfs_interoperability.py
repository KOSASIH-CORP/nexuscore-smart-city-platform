import ipfshttpclient

class IPFSInteroperability:
    def __init__(self, ipfs_url):
        self.ipfs_url = ipfs_url
        self.client = ipfshttpclient.connect(self.ipfs_url)

    def add_file(self, file_path):
        response = self.client.add(file_path)
        return response['Hash']

    def get_file(self, file_hash):
        response = self.client.cat(file_hash)
        return response

    def pin_file(self, file_hash):
        response = self.client.pin.add(file_hash)
        return response

    def unpin_file(self, file_hash):
        response = self.client.pin.rm(file_hash)
        return response
