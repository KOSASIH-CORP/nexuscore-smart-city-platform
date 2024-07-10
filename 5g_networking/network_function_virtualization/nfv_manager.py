import requests

class NFVManager:
    def __init__(self, api_url):
        self.api_url = api_url

    def create_vnf(self, vnf_name, vnf_description):
        response = requests.post(self.api_url, json={'name': vnf_name, 'description': vnf_description})
        return response.json()

    def delete_vnf(self, vnf_id):
        response = requests.delete(f"{self.api_url}/{vnf_id}")
        return response.status_code
