pragma solidity ^0.8.0;

contract SmartCityContract {
    address private owner;
    mapping (address => uint256) public deviceData;

    constructor() public {
        owner = msg.sender;
    }

    function addDeviceData(address deviceAddress, uint256 data) public {
        require(msg.sender == owner, "Only the owner can add device data");
        deviceData[deviceAddress] = data;
    }

    function getDeviceData(address deviceAddress) public view returns (uint256) {
        return deviceData[deviceAddress];
    }
}
