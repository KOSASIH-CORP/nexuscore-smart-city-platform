import ipfshttpclient

class IPFSStorage:
    def __init__(self, ipfs_api_url):
        self.ipfs_api_url = ipfs_api_url
        self.client = ipfshttpclient.connect(self.ipfs_api_url)

    def store_data(self, data):
        response = self.client.add(data)
        return response['Hash']

    def retrieve_data(self, hash):
        response = self.client.cat(hash)
        return response
