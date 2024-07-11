class Block {
    constructor(data) {
        this.data = data;
        this.hash = this.calculateHash();
    }

    calculateHash() {
        // Implement hash calculation logic
        return "hash-" + Math.random().toString(36).substr(2, 9);
    }
}

class Blockchain {
    constructor() {
        this.chain = [this.createGenesisBlock()];
    }

    createGenesisBlock() {
        return new Block("Genesis Block");
    }

    addBlock(block) {
        this.chain.push(block);
    }

    getBlock(hash) {
        return this.chain.find((block) => block.hash === hash);
    }
}

module.exports = { Block, Blockchain };
