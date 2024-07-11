const Web3 = require("web3");
const contract = require("./SmartCityContract.sol");

class BlockchainUtils {
    constructor() {
        this.web3 = new Web3(new Web3.providers.HttpProvider("https://mainnet.infura.io/v3/YOUR_PROJECT_ID"));
        this.contract = new this.web3.eth.Contract(contract.abi, contract.address);
    }

    async addDeviceData(deviceAddress, data) {
        const txCount = await this.web3.eth.getTransactionCount();
        const tx = {
            from: "0xYOUR_WALLET_ADDRESS",
            to: contract.address,
            value: "0",
            gas: "20000",
            gasPrice: "20",
            data: this.contract.methods.addDeviceData(deviceAddress, data).encodeABI(),
        };
        const signedTx = await this.web3.eth.accounts.signTransaction(tx, "0xYOUR_WALLET_PRIVATE_KEY");
        await this.web3.eth.sendSignedTransaction(signedTx.rawTransaction);
    }

    async getDeviceData(deviceAddress) {
        return await this.contract.methods.getDeviceData(deviceAddress).call();
    }
}

module.exports = BlockchainUtils;
