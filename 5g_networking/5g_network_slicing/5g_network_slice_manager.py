import json

class FiveGNetworkSliceManager:
    def __init__(self, network_slice_config):
        self.network_slice_config = network_slice_config
        self.network_slices = {}

    def create_network_slice(self, slice_id, slice_config):
        self.network_slices[slice_id] = slice_config

    def update_network_slice(self, slice_id, slice_config):
        self.network_slices[slice_id] = slice_config

    def delete_network_slice(self, slice_id):
        del self.network_slices[slice_id]

    def get_network_slice(self, slice_id):
        return self.network_slices.get(slice_id)

    def get_all_network_slices(self):
        return self.network_slices
