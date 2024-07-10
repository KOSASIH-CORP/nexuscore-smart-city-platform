import indy
from indy import wallet

class SelfSovereignIdentityWalletDID:
    def __init__(self, wallet_name, wallet_key, did_method, did_key):
        self.wallet_name = wallet_name
        self.wallet_key = wallet_key
        self.did_method = did_method
        self.did_key = did_key
        self.wallet = wallet.open_wallet(self.wallet_name, self.wallet_key)
        self.did, self.verkey = wallet.create_did(self.wallet, self.did_method, self.did_key)

    def create_credential_definition(self, cred_def_id, cred_def_json):
        cred_def = wallet.create_credential_definition(self.wallet, cred_def_id, cred_def_json)
        return cred_def

    def store_credential(self, cred_id, cred_values):
        cred_req = wallet.store_credential(self.wallet, cred_id, cred_values)
        return cred_req

    def get_credential(self, cred_id):
        cred = wallet.get_credential(self.wallet, cred_id)
        return cred

    def sign_credential(self, cred_id, signature_type):
        signature = wallet.sign_credential(self.wallet, cred_id, signature_type)
        return signature
