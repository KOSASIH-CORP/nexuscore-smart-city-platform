import requests

class NetworkSliceOrchestrator:
    def __init__(self, api_url):
        self.api_url = api_url

    def create_network_slice(self, slice_name, slice_description):
        response = requests.post(self.api_url, json={'name': slice_name, 'description': slice_description})
        return response.json()

    def delete_network_slice(self, slice_id):
        response = requests.delete(f"{self.api_url}/{slice_id}")
        return response.status_code
