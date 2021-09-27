# PoA - Guide

Proof of Authority (PoA) is consensus algorithm that provides high performance and fault tolerance. In PoA, rights to generate new blocks are awarded to nodes that have proven their authority to do so. To gain this authority and a right to generate new blocks, a node must pass a preliminary authentication. This kind of consensus algorithm is used with permissioned blockchain.

## PoA based Blockchaian

#### Node Details

For the purpose of this homework, same password has been used to create the nodes. Password is 'BlockTestNet'

##### <b>Node1 : Public address - 0x41236dCCf34bd49E2697166b58003cD7350dF189</b>
##### <b>Node2 : Public address - 0x8F19d7EC50ee9Fb866A408D3a62fe1233529e28c</b>

### Creating Blockchain

Network Details:

##### <b>Network Name :  blockchain_hw_testnet</b>
##### <b>ChainID : 5000</b>

Run the following commands to initialise the nodes.

```
./geth --datadir /Users/hemanglunagaria/Documents/Monash_FinTech_repos/multi_blockchain_wallet_python/PoA/node1  init /Users/hemanglunagaria/Documents/Monash_FinTech_repos/multi_blockchain_wallet_python/PoA/test_net.json 

./geth --datadir /Users/hemanglunagaria/Documents/Monash_FinTech_repos/multi_blockchain_wallet_python/PoA/node2  init /Users/hemanglunagaria/Documents/Monash_FinTech_repos/multi_blockchain_wallet_python/PoA/test_net.json 
```

### Running the nodes

#### Node 1 : 

```
./geth --datadir /Users/hemanglunagaria/Documents/Monash_FinTech_repos/multi_blockchain_wallet_python/PoA/node1  --unlock "41236dCCf34bd49E2697166b58003cD7350dF189" --mine --port 30308 --rpc --allow-insecure-unlock
```

Flags:

1. --datadir : Data directory for the databases and keystore
2. --unlock : Account to unlock. It can take multiple values.
3. --mine : Enable mining
4. --port :  Port on which network node is listening
5. --rpc : Enable HTTP-RPC server (deprecated and will be removed in future versions, replaced with --http)
6. --allow-insecure-unlock : Allow insecure account unlocking when account-related RPCs are exposed by http

#### Node 2 :

./geth --datadir /Users/hemanglunagaria/Documents/Monash_FinTech_repos/multi_blockchain_wallet_python/PoA/node2  --unlock "8F19d7EC50ee9Fb866A408D3a62fe1233529e28c" --mine --port 30311 --bootnodes "enode://a093359bec93d693a76bd740052de32e043f946d0cbbac69766d3d04faf8e4441b1ae7e35a7db602ac0089a24a9771e72e3f12409d49010e4b8edbf31129bb41@127.0.0.1:30310" --allow-insecure-unlock

Flags:

1. --datadir : Data directory for the databases and keystore
2. --unlock : Account to unlock. It can take multiple values.
3. --mine : Enable mining
4. --port :  Port on which network node is listening
5. --bootnodes : Comma separated enode URLs for P2P discovery bootstrap
6. --allow-insecure-unlock : Allow insecure account unlocking when account-related RPCs are exposed by http
