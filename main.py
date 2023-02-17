from fastapi import FastAPI
from web3 import Web3
from constants.abi import contract_abi
from constants.constants import contract_address
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Connect to the blockchain network
w3 = Web3(Web3.HTTPProvider("https://core.bloxberg.org"))
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Load the account from a private key
private_key = os.getenv('PRIVATE_KEY')
account = w3.eth.account.from_key(private_key)
w3.eth.defaultAccount = account.address  # Set the account as the default account


@app.get("/")
async def root():
    tx = contract.functions.addUserPermission(10, 10).build_transaction({
        'gas': 200000,
        'gasPrice': w3.toWei('1.05', 'gwei'),
        'nonce': w3.eth.get_transaction_count(w3.eth.defaultAccount),
    })

    signed_txn = w3.eth.account.sign_transaction(tx, private_key=private_key)

    t = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

    print(t.hex())


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
