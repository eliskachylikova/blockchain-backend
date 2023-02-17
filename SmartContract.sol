// SPDX-License-Identifier: MIT
pragma solidity ^0.7.0;
pragma abicoder v2;

contract Hackathon {

    address private owner; // creator of the contract

    mapping (uint => mapping(uint => bool)) groupPermissions; // group's permissions to a room
    mapping (uint => mapping(uint => bool)) userPermissions; // user's permissions to a room

    mapping (string => mapping(string => bool)) guidePermissions; //user's permissions to a guides
    string[] allGuides;

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
        userPermissions[_userId][_roomId] = true;
        emit UserPermissionGranted(_userId, _roomId, block.timestamp);
    }

    function revokeUserPermission(uint _userId, uint _roomId) public onlyOwner {
        userPermissions[_userId][_roomId] = false;
    }


    function addGroupPermission(uint _groupId, uint _roomId) public onlyOwner {
        groupPermissions[_groupId][_roomId] = true;
        emit GroupPermissionGranted(_groupId, _roomId, block.timestamp);

    }

    function revokeGroupPermission(uint _groupId, uint _roomId) public onlyOwner {
        groupPermissions[_groupId][_roomId] = false;
    }


    function addGuidePermission(string memory _username, string memory _guideId) public onlyOwner {
        guidePermissions[_username][_guideId] = true;

        bool containsValue = false;

        for(uint i = 0; i < allGuides.length; i++) {
            if (keccak256(abi.encodePacked(allGuides[i])) == keccak256(abi.encodePacked(_guideId))) {
                containsValue = true;
                break;
            }
        }

        if (!containsValue) {
            allGuides.push(_guideId);
        }

    }

    function revokeGuidePermission(string memory _username, string memory _guideId) public onlyOwner {
        guidePermissions[_username][_guideId] = false;
    }


    function checkUserPermission(uint _userId, uint _roomId) public view returns (bool) {
        return userPermissions[_userId][_roomId];
    }

    function checkGroupPermission(uint _groupId, uint _roomId) public view returns (bool) {
        return groupPermissions[_groupId][_roomId];
    }

    function getGuidesByUsername(string memory _username) public view returns (string[] memory) {

        uint numGuides = 0;
        // count the number of guide names that have been granted permissions to the given username
        for (uint i = 0; i < allGuides.length; i++) {
            if (guidePermissions[_username][allGuides[i]]) {
                numGuides++;
            }
        }

        string[] memory guides = new string[](numGuides);
        uint index = 0;

        // populate the array with the guide names that have been granted permissions to the given username
        for (uint i = 0; i < allGuides.length; i++) {
            if (guidePermissions[_username][allGuides[i]]) {
                guides[index] = allGuides[i];
                index++;
            }
        }
        return guides;
    }

}