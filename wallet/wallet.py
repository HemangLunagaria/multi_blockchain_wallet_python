# Import dependencies
import subprocess
import json
import os

from web3 import Web3
from eth_account import Account
from web3.middleware import geth_poa_middleware

from bit import PrivateKeyTestnet
from bit.network import NetworkAPI
# from bit import wif_to_key

from dotenv import load_dotenv

from constants import *

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Load and set environment variables
load_dotenv()
mnemonic=os.getenv("mnemonic")
# print(mnemonic)
 
# Create a function called `derive_wallets`
def derive_wallets(coin):
    command =  f"./derive -g --mnemonic='{mnemonic}' --cols=path,address,privkey,pubkey --coin={coin} --numderive=3 --format=json"
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    keys = json.loads(output)
    return keys

# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = {}
coins[ETH] = derive_wallets(ETH)
coins[BTCTEST] = derive_wallets(BTCTEST)
# print(coins)

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(coin, priv_key):
    if (coin == ETH):
        return Account.from_key(priv_key)
    elif (coin == BTCTEST):
        return PrivateKeyTestnet(priv_key)
        # return wif_to_key(priv_key)

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(coin, account, to, amount):
    if (coin == ETH):
        return create_eth_tx(account, to, amount)
    elif (coin ==BTCTEST):
        # tx = []
        # tx.append((to, amount, BTC))
        # return tx
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])

def create_eth_tx(account, recipient, amount):
    gasEstimate = w3.eth.estimateGas(
        {"from": account.address, "to": recipient, "value": amount}
    )
    return {
        "chainId":w3.eth.chain_id,
        "from": account.address,
        "to": recipient,
        "value": amount,
        "gasPrice": w3.eth.gasPrice,
        "gas": gasEstimate,
        "nonce": w3.eth.getTransactionCount(account.address),
    }

# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(coin, priv_key_account, to, amount):
    if (coin == ETH):
        account = priv_key_to_account(coin, priv_key_account)
        raw_tx = create_tx(coin, account, to , amount)
        signed_tx = account.sign_transaction(raw_tx)
        result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(result.hex())
    elif (coin == BTCTEST):
        account = priv_key_to_account(coin, priv_key_account)
        tx = create_tx(coin, account, to, amount)
        signed = account.sign_transaction(tx)
        NetworkAPI.broadcast_tx_testnet(signed)
        print(account.get_transactions()[0])
