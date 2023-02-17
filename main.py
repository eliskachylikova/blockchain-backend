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


@app.get("/store")
async def store(number: int):
    # Call the smart contract function to save the data
    tx_hash = contract.functions.store(number).transact()

    # Wait for the transaction to be mined
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    # Return the transaction receipt to the client
    return receipt


@app.get("/")
async def root():
    # print(w3.eth.get_block('latest'))
    # return {"message": w3.eth.get_block('latest')}
    return {"message": "Hello"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
