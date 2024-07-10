import eth_utils

class SolidityContract:
    def __init__(self, contract_abi, contract_address):
        self.contract_abi = contract_abi
        self.contract_address = contract_address
        self.contract = eth_utils.Interface(self.contract_abi)

    def call_function(self, function_name, *args):
        function = self.contract.get_function_by_name(function_name)
        result = function(*args)
        return result
