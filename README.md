![Komodo_Logo](logo.png?raw=true)
# Komodo RPC API Library

#### RPC API-Library for Komodo-based asset chains, for Python Developers.
===============================================================================
### Description:
- #### Komodo-RPC library helps you integrate your Python Apps with Komodo asset-chains without having to setup/implement required RPC functions. Install this Python library and call Komodo-API RPCs as easily as calling a local function. Komodo-RPC library acts as a wrapper between your Python app and the Komodo-daemon running on a server.
#####
### Installation:
#### Install 'komodorpc' Python Module:
  - > ` pip install komodorpc `
  
### Usage:
``` {.sourceCode .python}
>>> from komodo_rpc import KomodoRPC
>>> import komodo.wallet as wallet
>>> komodo_rpc = KomodoRPC(node_addr='127.0.0.1', rpc_port=98102, req_method='POST', rpc_username='user71631186',
...                         rpc_password='pass725b1d10ae0c2217a8ffbgh30e5ca13367afvdl937bf1cbq11bd16f8a1e36d30')
>>> result = wallet.getwalletinfo()
>>> result
'{"result":{"walletversion":60000,"balance":2000000.16063408,"unconfirmed_balance":0.00000000,"immature_balance":0.00000000,"txcount":15,"keypoololdest":1561025064,"keypoolsize":101,"paytxfee":0.00000000,"seedfp":"7bd4d97c90d68f5921fee04e63168bd956d63346bf011c80d46e75b134385c"},"error":null,"id":"curltest"}\n'
>>> 
```
 - #### Create an object of **KomodoRPC** class with following parameters to populate RPC options and authentication parameters.
 |   Argument   |                                   Description                                   |
|:------------:|:-------------------------------------------------------------------------------:|
|   node_addr  | IP address of the node where the Komodo-daemon is running; **Default: '127.0.0.1'** |
|   rpc_port   |            Port number where the Komodo-daemon is listening for RPCs            |
| rpc_username |                         Username for RPC authentication                         |
| rpc_password |                         Password for RPC authentication                         |
|  req_method  |                     Request Method for RPCs; Default: 'POST'                    |
|  jsonrpc_ver |                              **Default:'1.0'**                                  |
|  rpc_req_id  |                     ID for RPC requests **Default:'curltest'**                  |

 ``` {.sourceCode .python}
 >>> from komodo_rpc import KomodoRPC
 >>> komodo_rpc = KomodoRPC( node_addr='127.0.0.1',
                         rpc_port='4524', 
                         req_method='POST', 
                         rpc_username='user32703390897', 
                         rpc_password='pass885b1d876131e0c2217a848ffbf5fe5ca34367af529a6d519abf8cbb5bd16f8a1e36d30'
               )
 ```
#####
- #### API commands are segregated into different modules:
|          Module         |                                                                                                                                                                               Description                                                                                                                                                                               |
|:-----------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|      komodo.address     |  Includes all address-related commands.<br> Example: <br> ```  import komodo.address as address ``` <br> ```  result = address.getaddressbalance(addresses=["RMTTgkYk6r5kCYiWGmoihdts61XZ"]) ```                                                                                                                                                                  |
|    komodo.blockchain    | Includes all blockchain-related commands.<br> Example: <br> ```  import komodo.blockchain as blockchain ``` <br> ```  result = blockchain.getbestblockhash() ```                                                                                                                                                                                                  |
|      komodo.control     | Includes all Control commands.<br>  Example: <br> ```   import komodo.control as control ``` <br> ```  result = control.help(command='getwalletinfo') ```                                                                                                                                                                                    |
|    komodo.disclosure    | Includes all disclosure-related commands. <br>  Example: <br> ```   import komodo.disclosure as disclosure``` <br> ```  result = disclosure.z_validatepaymentdisclosure(paymentdisclosure='zpd:76462047b6c204') ```                                                                                            |
|     komodo.generate     | Includes all Generation commands. <br>  Example:<br> ```   import komodo.generate as generate``` <br> ```  result = generate.setgenerate(generate=False, genproclimit=2) ```                                                                                                                                                                 |
|      komodo.jumblr      | Includes all Jumblr commands.<br>  Example: <br>   ``` import komodo.jumblr as jumblr``` <br> ```  result = jumblr.jumblr_deposit(depositaddress='RT4SUjG3QeGcedfpHtP5MhDeEGTA') ```                                                                                                                                                         |
|      komodo.mining      | Includes all mining-related commands. <br>  Example: <br> ```   import komodo.mining as mining``` <br> ```  result = mining.getmininginfo() ```                                                                                                                                                                                              |
|      komodo.network     | Includes all network-related commands. <br>  Example:<br> ```   import komodo.network as network``` <br> ``` result = network.getnetworkinfo() ```                                                                                                                                                                                                      |
| komodo.raw_transactions | Includes all raw_transactions commands. <br>  Example: <br> ```   import komodo.raw_transactions as raw_transactions``` <br> ```  result = raw_transactions.createrawtransaction(transactions={'ff2c4c0c0d55310c9e1b7f193d7f69d7a5b662fc610':0},amounts={'R9fZXs2M6YiTNCQKqgPC4mR4cE3VQkAGzW':0.001}) ``` |
|       komodo.util       | Includes all utility-related commands.<br>  Example: <br> ```   import komodo.util as util``` <br> ```  result = util.estimatepriority(num_blocks=2) ```                                                                                                                                                                                     |
|      komodo.wallet      | Includes all wallet-related commands. <br>  Example:<br> ```  import komodo.wallet as wallet``` <br> ```  result = wallet.getwalletinfo() ```                                                                                                                                                                                                                     |
#####
### Documentation:
- #### [Komodo API Guide](https://developers.komodoplatform.com/basic-docs/komodo-api/)

