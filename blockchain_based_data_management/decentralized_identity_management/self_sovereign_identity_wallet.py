import indy
from indy import wallet

class SelfSovereignIdentityWallet:
    def __init__(self, wallet_name, wallet_key):
        self.wallet_name = wallet_name
        self.wallet_key = wallet_key
        self.wallet = wallet.open_wallet(self.wallet_name, self.wallet_key)

    def create_did(self, did_method, did_key):
        did, verkey = wallet.create_did(self.wallet, did_method, did_key)
        return did, verkey

    def store_credential(self, cred_def_id, cred_values):
        cred_req = wallet.store_credential(self.wallet, cred_def_id, cred_values)
        return cred_req

    def get_credential(self, cred_id):
        cred = wallet.get_credential(self.wallet, cred_id)
        return cred

    def sign_credential(self, cred_id, signature_type):
        signature = wallet.sign_credential(self.wallet, cred_id, signature_type)
        return signature
