from fastapi import FastAPI
from web3 import Web3
from constants.abi import contract_abi
from constants.constants import contract_address
import os
from dotenv import load_dotenv
from pydantic import BaseModel


load_dotenv()
app = FastAPI()

# Connect to the blockchain network
w3 = Web3(Web3.HTTPProvider("https://core.bloxberg.org"))
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Load the account from a private key
private_key = os.getenv('PRIVATE_KEY')
account = w3.eth.account.from_key(private_key)
w3.eth.defaultAccount = account.address  # Set the account as the default account


@app.get("/assign_user_permission", tags=['Permissions'], summary="Assign permission for a user to control devices in a room")
async def assign_user_permission(user_id: int, room_id: int):
    tx = contract.functions.addUserPermission(user_id, room_id).build_transaction({
        'gas': 200000,
        'gasPrice': w3.to_wei('1.05', 'gwei'),
        'nonce': w3.eth.get_transaction_count(w3.eth.defaultAccount),
    })

    signed_txn = w3.eth.account.sign_transaction(tx, private_key=private_key)

    t = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

    print(t.hex())


@app.get("/assign_group_permission", tags=['Permissions'], summary="Assign permission for a group to control devices in a room")
async def assign_group_permission(group_id: int, room_id: int):
    tx = contract.functions.addGroupPermission(group_id, room_id).build_transaction({
        'gas': 200000,
        'gasPrice': w3.to_wei('1.05', 'gwei'),
        'nonce': w3.eth.get_transaction_count(w3.eth.defaultAccount),
    })

    signed_txn = w3.eth.account.sign_transaction(tx, private_key=private_key)

    t = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

    print(t.hex())


@app.get("/check_user_permission", tags=['Permissions'], summary="Check if a user has a permission to control a room")
async def check_user_permission(user_id: int, room_id: int):
    return contract.functions.checkUserPermission(user_id, room_id).call()


@app.get("/check_group_permission", tags=['Permissions'], summary="Check if a group has a permission to control a room")
async def check_group_permission(group_id: int, room_id: int):
    return contract.functions.checkGroupPermission(group_id, room_id).call()


class Request(BaseModel):
    username: str


@app.post("/guides", tags=['Guides'], summary="Returns list of guides for a user by their username")
async def get_guides_by_user(request: Request):
    print(contract.functions.getGuidesByUsername(request.username).call())
    return request.username



