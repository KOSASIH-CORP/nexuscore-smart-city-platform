import requests

class MECOrchestrator:
    def __init__(self, api_url):
        self.api_url = api_url

    def create_mec_host(self, host_name, host_description):
        response = requests.post(self.api_url, json={'name': host_name, 'description': host_description})
        return response.json()

    def delete_mec_host(self, host_id):
        response = requests.delete(f"{self.api_url}/{host_id}")
        return response.status_code
