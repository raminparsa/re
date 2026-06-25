from web3 import Web3
from web 2
w3 = Web3(Web3.HTTPProvider("https://sepolia.base.org"))
cfbcfczui87ii
private_key = "YOUR_PRIVATE_KEY"
account = w3.eth.account.from_key(private_key)tyd
,.yuopy777t78
contract_address = "0x0000000000000000000000000000000000000000"
rrtyuyuyyuydfhdfy
abi = [{okoko
    "inputs":[{"name":"value","type":"uint256"}]erte4,
    "name":"setValue",rtyr55
    "outputs":[],
    "stateMutabiliwerty":"nonpayable",
    "type":"function"eryrey
}]ufkjygygoppk7846461351tryhr 
cfgfcvty12
contract = w3.eth.contract(address=contract_address, abi=abi)[p
cccffg
tx = contract.functions.setValue(123).build_transaction({
    "from": account.address,
    "nonce": w3.eth.get_transaction_count(account.address),
    "gas": 100000,
    "gasPrice": w3.eth.gas_price,
    "chainId": 84532
})uytfuy
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
/okoio/weg
