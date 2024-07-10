import requests

class NetworkSliceManager:
    def __init__(self, network_slice_api_url):
        self.network_slice_api_url = network_slice_api_url

    def create_network_slice(self, slice_name, slice_description):
        response = requests.post(self.network_slice_api_url, json={'name': slice_name, 'description': slice_description})
        return response.json()

    def delete_network_slice(self, slice_id):
        response = requests.delete(f"{self.network_slice_api_url}/{slice_id}")
        return response.status_code
