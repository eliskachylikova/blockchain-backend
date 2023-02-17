from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://rpc.sepolia.dev/"))
print(w3.eth.get_block('latest'))
