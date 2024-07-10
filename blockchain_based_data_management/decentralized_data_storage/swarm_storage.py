import swarm

class SwarmStorage:
    def __init__(self, swarm_url):
        self.swarm_url = swarm_url
        self.client = swarm.Client(self.swarm_url)

    def upload_file(self, file_path):
        response = self.client.upload(file_path)
        return response['Hash']

    def download_file(self, file_hash):
        response = self.client.download(file_hash)
        return response

    def list_files(self):
        response = self.client.list()
        return response
