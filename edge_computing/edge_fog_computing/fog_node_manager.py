import docker

class FogNodeManager:
    def __init__(self, fog_node_ip_address):
        self.fog_node_ip_address = fog_node_ip_address
        self.client = docker.DockerClient(base_url=f"http://{self.fog_node_ip_address}:2375")

    def deploy_container(self, container_image):
        container = self.client.containers.run(container_image, detach=True)
        return container.id

    def stop_container(self, container_id):
        container = self.client.containers.get(container_id)
        container.stop()
