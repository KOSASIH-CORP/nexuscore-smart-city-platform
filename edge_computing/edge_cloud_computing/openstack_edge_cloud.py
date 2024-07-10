import openstack

class OpenStackEdgeCloud:
    def __init__(self, auth_url, username, password, project_name):
        self.auth_url = auth_url
        self.username = username
        self.password = password
        self.project_name = project_name
        self.conn = openstack.connect(auth_url=self.auth_url, username=self.username, password=self.password, project_name=self.project_name)

    def create_server(self, server_name, image_id, flavor_id):
        server = self.conn.compute.create_server(name=server_name, image_id=image_id, flavor_id=flavor_id)
        return server

    def delete_server(self, server_id):
        self.conn.compute.delete_server(server_id)
