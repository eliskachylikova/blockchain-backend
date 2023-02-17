// SPDX-License-Identifier: MIT
pragma solidity ^0.7.0;

contract Hackathon {

    address private owner; // creator of the contract

    mapping (uint => mapping(uint => bool)) groupPermission; // group's permissions to a room
    mapping (uint => mapping(uint => bool)) userPermission; // user's permissions to a room

    event GroupPermissionGranted(uint groupId, uint roomId, uint date);

    event UserPermissionGranted(uint userId, uint roomId, uint date);


    // Only creator of the contract can run some operations
    modifier onlyOwner {
        require(msg.sender == owner);
        _; // rest of the function body where this modifier is used
    }

    constructor() {
        owner = msg.sender;
    }

    function addUserPermission(uint _userId, uint _roomId) public onlyOwner {
        userPermission[_userId][_roomId] = true;
        emit UserPermissionGranted(_userId, _roomId, block.timestamp);
    }

    function revokeUserPermission(uint _userId, uint _roomId) public onlyOwner {
        userPermission[_userId][_roomId] = false;
    }

    function addGroupPermission(uint _groupId, uint _roomId) public onlyOwner {
        groupPermission[_groupId][_roomId] = true;
    }

    function revokeGroupPermission(uint _groupId, uint _roomId) public onlyOwner {
        groupPermission[_groupId][_roomId] = false;
    }


    function checkUserPermission(uint _userId, uint _roomId) public view returns (bool) {
        return userPermission[_userId][_roomId];
    }

    function checkGroupPermission(uint _groupId, uint _roomId) public view returns (bool) {
        return groupPermission[_groupId][_roomId];
    }

}