import requests
from keystoneauth1.identity import v3
from keystoneauth1 import session

class NFVManagementOrchestrationOpenStack:
    def __init__(self, auth_url, username, password, project_name):
        self.auth_url = auth_url
        self.username = username
        self.password = password
        self.project_name = project_name
        self.auth = v3.Password(auth_url=auth_url, username=username, password=password, project_name=project_name)
        self.sess = session.Session(auth=self.auth)

    def create_vnf(self, vnf_name, vnf_description):
        response = requests.post(f"{self.auth_url}/vnfs", json={'name': vnf_name, 'description': vnf_description}, headers={'X-Auth-Token': self.sess.get_token()})
        return response.json()

    def delete_vnf(self, vnf_id):
        response = requests.delete(f"{self.auth_url}/vnfs/{vnf_id}", headers={'X-Auth-Token': self.sess.get_token()})
        return response.status_code

    def scale_vnf(self, vnf_id, scale_out):
        response = requests.patch(f"{self.auth_url}/vnfs/{vnf_id}", json={'scale_out': scale_out}, headers={'X-Auth-Token': self.sess.get_token()})
        return response.json()
