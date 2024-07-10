import docker

class EdgeDevice:
    def __init__(self, device_id):
        self.device_id = device_id
        self.docker_client = docker.from_env()

    def deploy_container(self, container_image):
        container = self.docker_client.containers.run(container_image, detach=True)
        return container

    def get_container_status(self, container_id):
        container = self.docker_client.containers.get(container_id)
        return container.status
