from web3 import Web3
from web 2
w3 = Web3(Web3.HTTPProvider("https://sepolia.base.org"))
cfbcfcz
private_key = "YOUR_PRIVATE_KEY"
account = w3.eth.account.from_key(private_key)
,.yuop
contract_address = "0x0000000000000000000000000000000000000000"
rrty
abi = [{
    "inputs":[{"name":"value","type":"uint256"}],
    "name":"setValue",
    "outputs":[],
    "stateMutability":"nonpayable",
    "type":"function"
}]
cfgfcvty12
contract = w3.eth.contract(address=contract_address, abi=abi)
cccffg
tx = contract.functions.setValue(123).build_transaction({
    "from": account.address,
    "nonce": w3.eth.get_transaction_count(account.address),
    "gas": 100000,
    "gasPrice": w3.eth.gas_price,
    "chainId": 84532
})
fggfdxcg
signed = w3.eth.account.sign_transaction(tx, private_key)
toyewt
print("Signed:", signed.hash.hex())
lklk5454
ertfgrtd
wwr34gfffgomnvvg
wer343ftghtth
hello baseyu
fthtfht
dtrtth
ftyytydfr
base
cexbase
figo
SSSfgd
