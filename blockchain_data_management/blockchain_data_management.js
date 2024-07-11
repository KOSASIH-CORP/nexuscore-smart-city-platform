const { Blockchain, Block } = require("./blockchain");

class BlockchainDataManagement {
    constructor() {
        this.blockchain = new Blockchain();
    }

    async addBlock(data) {
        const block = new Block(data);
        this.blockchain.addBlock(block);
        return block.hash;
    }

    async getBlock(hash) {
        return this.blockchain.getBlock(hash);
    }
}

module.exports = BlockchainDataManagement;
