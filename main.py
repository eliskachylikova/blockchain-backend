from fastapi import FastAPI
from web3 import Web3

app = FastAPI()


@app.get("/")
async def root():
    w3 = Web3(Web3.HTTPProvider("https://rpc.sepolia.dev/"))
    print(w3.eth.get_block('latest'))
    return {"message": w3.eth.get_block('latest')}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
