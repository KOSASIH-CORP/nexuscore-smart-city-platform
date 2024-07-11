const { Blockchain, Block } = require("./blockchain");

class DataManagementSystem {
    constructor() {
        this.blockchain = new Blockchain();
    }

    addData(data) {
        const block = new Block(data);
        this.blockchain.addBlock(block);
    }

    getData() {
        return this.blockchain.chain.map(block => block.data);
    }
}

module.exports = DataManagementSystem;
