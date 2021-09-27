# Multi Blockchain Wallet with Python

![Introduction](images/introduction.jpeg)

## Description

This project aims to create wallet that can interact with blockchain networks. As PoC, this wallet will integrate with Ethereum and Bitcoin Test coins. It has the ability to send transactions from addresses that are generated using hd-wallet-derive command line tool.

## Wallet - Code Details

### Step 1

Fund the test accounts with some seed coins for testing.

* BTCTEST - Using a test faucet, fund the address as below.

![Faucet](images/BTC_Faucet.png)

![BTC_Test_account](images/BTC_Test_account.png)

* ETH - Run a local PoA blockchain

More details on how to run the PoA blockchain locally can be found in the README inside PoA directory.

![Local_POA](images/ETH_Local_PoA.png)

![Local_ETH_account](images/ETH_Local_account.png)

### Step 2

Connect the python script to ETH Local blockchain via the below code

```
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
```
 bit library is used to connect to Bitcoin Test net.

 ### Step 3

 Run the python script in the Python shell

![Python Script](images/Python_script_running.png)

![ETH_transaction](images/ETH_transaction_pending.png)

![ETH_transaction](images/ETH_transaction_successful.png)

![BTC_Transaction](images/BTC_test_transaction.png)

Logic to retrieve the latest transaction id needs bit more fine tuning and also need better error handling.
