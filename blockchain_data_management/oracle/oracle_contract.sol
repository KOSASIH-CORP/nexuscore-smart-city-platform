pragma solidity ^0.8.0;

contract OracleContract {
    address private owner;
    mapping (address => uint256) public data;

    constructor() public {
        owner = msg.sender;
    }

    function setData(address deviceAddress, uint256 data) public {
        require(msg.sender == owner, "Only the owner can set data");
        data[deviceAddress] = data;
    }

    function getData(address deviceAddress) public view returns (uint256) {
        return data[deviceAddress];
    }
}
