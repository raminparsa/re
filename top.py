from web3 import Web3
y7iuiyu7
fthfngf 
ftujhghjop
RPC_URL = "https://sepolia.base.org"
w3 = Web3(Web3.HTTPProvider(RPC_URL))
vu/.;
if not w3.is_connected():
    raise Exception("Unable to connect")
cxvfy,.,l
address = "0xYourWalletAddress"
awfca grgrfg
balance = w3.eth.get_balance(address)
balance_eth = w3.from_wei(balance, "ether")
wertfdry
latest_block = w3.eth.block_number
sw ovuyfjm,irtyr,,
print(f"Wallet: {address}")
print(f"Balance: {balance_eth} ETH")
print(f"Latest Block: {latest_block}")

gas_price = w3.eth.gas_price

print(f"Gas Price: {w3.from_wei(gas_price, 'gwei')} Gwei")
54
rtgg
gtthhj
lolkk
