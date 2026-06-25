from web3 import Web3
lopdrtg
w3 = Web3(Web3.HTTPProvider("https://sepolia.base.org"))
fghhhh
private_key = "YOUR_PRIVATE_KEY"fgj
account = w3.eth.account.from_key(private_key)
cv;'/.dfhth
contract_address = "0x0000000000000000000000000000000000000000"
mk..hj
abi = [{pokop
    "inputs":[{"name":"value","type":"uint256"}],
    "name":"setValue",fghfgh
    "outputs"fth:fgh h[],fgh
    "stateMutability":"nonpayable",
    "type":"function"
}]ertnkiljytfghhhhdr
contract = w3.eth.contract(address=contract_address, abi=abi)
,.lopl;
tx = contract.functions.setValue(123).build_transaction({
    "from": account.address,
    "nonce": w3.eth.get_transaction_count(account.address),
    "gas": 100000,
    "gasPrice": w3.eth.gas_price,
    "chainId": 84532
})
xv,..opooij
signed = w3.eth.account.sign_transaction(tx, private_key)
65ygyu8hiuhui
print("Signed:", signed.hash.hex())lkop09
ty76
ty68
fgytre
vbqw./
