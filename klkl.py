from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://sepolia.base.org"))

private_key = "YOUR_PRIVATE_KEY"
account = w3.eth.account.from_key(private_key)

contract_address = "0x0000000000000000000000000000000000000000"

abi = [{
    "inputs":[{"name":"value","type":"uint256"}],
    "name":"setValue",
    "outputs":[],
    "stateMutability":"nonpayable",
    "type":"function"
}]

contract = w3.eth.contract(address=contract_address, abi=abi)

tx = contract.functions.setValue(123).build_transaction({
    "from": account.address,
    "nonce": w3.eth.get_transaction_count(account.address),
    "gas": 100000,
    "gasPrice": w3.eth.gas_price,
    "chainId": 84532
})

signed = w3.eth.account.sign_transaction(tx, private_key)

print("Signed:", signed.hash.hex())
lklk5454
ertfgrtd
wwr34gff
wer343
