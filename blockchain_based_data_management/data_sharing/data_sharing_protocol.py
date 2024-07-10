import hashlib

class DataSharingProtocol:
    def __init__(self, blockchain_network):
        self.blockchain_network = blockchain_network

    def share_data(self, data, recipient):
        data_hash = hashlib.sha256(data.encode()).hexdigest()
        transaction = self.blockchain_network.create_transaction(data_hash, recipient)
        self.blockchain_network.add_transaction(transaction)
        return transaction

    def verify_data(self, data, data_hash):
        if hashlib.sha256(data.encode()).hexdigest() == data_hash:
            return True
        return False
