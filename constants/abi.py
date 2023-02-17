contract_abi = [
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_groupId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_roomId",
                "type": "uint256"
            }
        ],
        "name": "addGroupPermission",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_userId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_roomId",
                "type": "uint256"
            }
        ],
        "name": "addUserPermission",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": "false",
        "inputs": [
            {
                "indexed": "false",
                "internalType": "uint256",
                "name": "groupId",
                "type": "uint256"
            },
            {
                "indexed": "false",
                "internalType": "uint256",
                "name": "roomId",
                "type": "uint256"
            },
            {
                "indexed": "false",
                "internalType": "uint256",
                "name": "date",
                "type": "uint256"
            }
        ],
        "name": "GroupPermissionGranted",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_groupId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_roomId",
                "type": "uint256"
            }
        ],
        "name": "revokeGroupPermission",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_userId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_roomId",
                "type": "uint256"
            }
        ],
        "name": "revokeUserPermission",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "anonymous": "false",
        "inputs": [
            {
                "indexed": "false",
                "internalType": "uint256",
                "name": "userId",
                "type": "uint256"
            },
            {
                "indexed": "false",
                "internalType": "uint256",
                "name": "roomId",
                "type": "uint256"
            },
            {
                "indexed": "false",
                "internalType": "uint256",
                "name": "date",
                "type": "uint256"
            }
        ],
        "name": "UserPermissionGranted",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_groupId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_roomId",
                "type": "uint256"
            }
        ],
        "name": "checkGroupPermission",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_userId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_roomId",
                "type": "uint256"
            }
        ],
        "name": "checkUserPermission",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]
