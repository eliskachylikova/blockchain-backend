from fastapi import FastAPI
from web3 import Web3
import json

app = FastAPI()

# Connect to the blockchain network
w3 = Web3(Web3.HTTPProvider("https://rpc.sepolia.dev/"))

# Load the smart contract ABI
with open('contract.abi', 'r') as f:
    contract_abi = json.load(f)

# Instantiate the smart contract
contract_address = '0xD8d1546c838091fDC3a01741eBfe1E8133560ecd'
contract = w3.eth.contract(address=contract_address, abi=contract_abi)


# Load the account from a private key
private_key = '450f187df076b5021adffec0f5a5aea216bd492c615d7a0be1fbfb788cf25522'
account = w3.eth.account.from_key(private_key)
w3.eth.defaultAccount = account.address  # Set the account as the default account


@app.get("/store")
async def store(num: int):
    print(num)

    # Construct the transaction object
    #nonce = w3.eth.getTransactionCount(w3.eth.defaultAccount)
    tx = {
        'from': w3.eth.defaultAccount,
        'to': contract_address,
        'gas': 2000000,
        'gasPrice': 1000,
        'nonce': 2,
        'data': contract.functions.store(5)#.encodeABI()
    }

    # Sign and send the transaction
    signed_tx = account.signTransaction(tx)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

    # Wait for the transaction to be mined
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    # Return the transaction receipt to the client
    return receipt

    #
    # # Call the smart contract function to save the data
    # tx_hash = contract.functions.store(number).transact()
    #
    # # Wait for the transaction to be mined
    # receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    #
    # # Return the transaction receipt to the client
    # return receipt


@app.get("/")
async def root():
    return {"message": "Hello"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
