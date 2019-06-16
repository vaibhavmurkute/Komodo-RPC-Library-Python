from komodo_rpc import KomodoRpc
import komodo.wallet as wallet
import komodo.network as network
import komodo.util as util
import komodo.address as address
import komodo.control as control
import komodo.raw_transactions as raw_transactions
import komodo.generate as generate
import komodo.mining as mining
import komodo.blockchain as blockchain
import komodo.disclosure as disclosure
import komodo.jumblr as jumblr

# set the authetication parameters and rpc port
komodo_rpc = KomodoRpc(node_addr='127.0.0.1', rpc_port=89181, req_method='POST', rpc_username='user31331008972',
                        rpc_password='pass885b1d82dsa131c2aw27a8ffbf5asdca34367af529a6d5aabf8cbbbasd16f6dfw0')

print('getwalletinfo: ')
result = wallet.getwalletinfo()
print(result)

print('getnetworkinfo: ')
result = network.getnetworkinfo()
print(result)

print('verifymessage: ')
result = util.verifymessage(signature='IHGQI9G1WpHBXqshBktuqXOJKRa6siPd+ZRWdBigZhZ6Mxdcz/qNMjyQRgZ2QKcSTNzL7tTC2A9TPfA0Xvc1M3c=', address='RMYTT9gkYk6r5kCY8ttiWGmoihdts61kXZ', message='Test Message')
print(result)

print('getaddressmempool: ')
result = address.getaddressmempool(addresses=["RMYTT9gkYk6r5kCY8ttiWGmoihdts61kXZ"])
print(result)

print('getinfo: ')
result = control.getinfo()
print(result)

print('z_getnewaddress: ')
result = wallet.z_getnewaddress()
print(result)

print('createrawtransaction: ')
result = raw_transactions.createrawtransaction(transactions={'ff2c4c0c0d55310c2f7e9105e2fdbdb1496049e1b7f193d7f69d7a5b662fc610':0}, amounts={'R9fZXs2M6YiTNCQKqgPC4mR4cE3VQkAGzW':0.001})
print(result)

print('getgenerate: ')
result = generate.getgenerate()
print(result)

print('getmininginfo: ')
result = mining.getmininginfo()
print(result)

print('getbestblockhash: ')
result = blockchain.getbestblockhash()
print(result)

print('z_getpaymentdisclosure: ')
result = disclosure.z_getpaymentdisclosure(txid='96f12882450429324d5f3b48630e3168220e49ab7b0f066e5c2935a6b88bb0f2', js_index=0, output_index=0, message='test')
print(result)

print('jumblr_pause: ')
result = jumblr.jumblr_pause()
print(result)
