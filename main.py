from fastapi import FastAPI
from web3 import Web3
from constants.abi import contract_abi
from constants.constants import contract_address

app = FastAPI()

# Connect to the blockchain network
# w3 = Web3(Web3.HTTPProvider("https://rpc.sepolia.dev/"))
# w3 = w3.eth.contract(address='0x7b02eF83aF1541338F6616e9A4D7115fF7091781', abi=abi)
w3 = Web3(Web3.HTTPProvider("https://core.bloxberg.org"))
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Load the account from a private key
private_key = '450f187df076b5021adffec0f5a5aea216bd492c615d7a0be1fbfb788cf25522'
account = w3.eth.account.from_key(private_key)
w3.eth.defaultAccount = account.address  # Set the account as the default account


@app.get("/store")
async def store():

    # Construct the transaction object
    # nonce = w3.eth.getTransactionCount(w3.eth.defaultAccount)

    tx = {
        'from': w3.eth.defaultAccount,
        'gas': 90000,
        'gasPrice': 1000000,
        'nonce': 1,
        'data': contract.functions.addUserPermission(1, 101).transact()  # .encodeABI()
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
    print(contract.functions.checkUserPermission(1, 102).call())


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
