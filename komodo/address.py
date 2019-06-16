import rpc_util.rpc as rpc

def getaddressbalance(addresses=[""]):
    '''
    The getaddressbalance method returns the confirmed balance for an address, or addresses. It requires addressindex to be enabled
    :param addresses: [string]	a list of addresses
    :return: JSON string containing:
        "balance"	(number)	the current confirmed balance in satoshis
        "received"	(number)	the total confirmed number of satoshis received (including change)
    '''
    addr_list = "["
    for addr in addresses:
        addr_list += "\"" + str(addr) + "\","
    if (len(addresses) > 0):
        addr_list = addr_list[:-1]
    addr_list += "]"
    data = '{'+rpc.get_request_metadata()+', "method": "getaddressbalance", "params": [{"addresses": ' + str(addr_list) + '}] }'
    return rpc.rpc_request(data)


def getaddressdeltas(addresses=[""], start=0, end=0, chainInfo=False):
    '''
    The getaddressdeltas method returns all confirmed balance changes of an address.
    :param addresses: [string]	a list of addresses
    :param start: (number)	the start block height
    :param end: (number)	the end block height
    :param chainInfo:(boolean)	include chain info in results (only applies if start and end specified)
    :return: JSON string containing:
        "satoshis"	(number)	the difference in satoshis
        "txid"	(string)	the related transaction id
        "index"	(number)	the related input or output index
        "height"	(number)	the block height
        "address"	(string)	the address
    '''
    addr_list = "["
    for addr in addresses:
        addr_list += "\"" + str(addr) + "\","
    if (len(addresses) > 0):
        addr_list = addr_list[:-1]
    addr_list += "]"
    data = '{'+rpc.get_request_metadata()+', "method": "getaddressdeltas", "params": [{"addresses": ' + str(addr_list) + ',"start":' + str(start) + ',"end":' + str(end) + ',"chainInfo":' + str(chainInfo).lower() + '}]}'
    return rpc.rpc_request(data)


def getaddressmempool(addresses=[""]):
    '''
    The getaddressmempool method returns all mempool deltas for an address, or addresses. It requires addressindex to be enabled.
    :param addresses: [string] a list of addresses
    :return: JSON string containing:
        "address"	(string)	the address
        "txid"	(string)	the related txid
        "index"	(number)	the related input or output index
        "satoshis"	(number)	the difference in satoshis
        "timestamp"	(number)	the time the transaction entered the mempool (seconds)
        "prevtxid"	(string)	the previous txid (if spending)
        "prevout"	(string)	the previous transaction output index (if spending)
    '''
    addr_list = "["
    for addr in addresses:
        addr_list += "\"" + str(addr) + "\","
    if (len(addresses) > 0):
        addr_list = addr_list[:-1]
    addr_list += "]"
    data = '{'+rpc.get_request_metadata()+', "method": "getaddressmempool", "params": [{"addresses": ' + str(addr_list) + '}] }'
    return rpc.rpc_request(data)


def getaddresstxids(addresses=[""], start=0, end=0):
    '''
    The getaddresstxids method returns the txids for an address, or addresses. It requires addressindex to be enabled.
    :param addresses: [string] a list of addreses
    :param start: (number)	the start block height
    :param end: (number)	the end block height
    :return: "transaction_id"	(JSON string)	the transaction id
    '''
    addr_list = "["
    for addr in addresses:
        addr_list += "\"" + str(addr) + "\","
    if (len(addresses) > 0):
        addr_list = addr_list[:-1]
    addr_list += "]"
    data = '{'+rpc.get_request_metadata()+', "method": "getaddresstxids", "params": [{"addresses": ' + str(addr_list) + ', "start":' + str(start) + ',"end":' + str(end) + '}] }'
    return rpc.rpc_request(data)


def getaddressutxos(addresses=[""], chainInfo=False):
    '''
    The getaddressutxos method returns all unspent outputs for an address. It requires addressindex to be enabled.
    :param addresses: [string] a list of addreses
    :param chainInfo: (boolean)	include chain info with results
    :return: JSON string containing:
        "address"	(string)	the address
        "txid"	(string)	the output txid
        "height"	(number)	the block height
        "outputIndex"	(number)	the output index
        "script"	(string)	the script hex encoded
        "satoshis"	(number)	the number of satoshis of the output
    '''
    addr_list = "["
    for addr in addresses:
        addr_list += "\"" + str(addr) + "\","
    if (len(addresses) > 0):
        addr_list = addr_list[:-1]
    addr_list += "]"
    data = '{'+rpc.get_request_metadata()+', "method": "getaddressutxos", "params": [{"addresses": ' + str(addr_list) + ', "chainInfo": ' + str(chainInfo).lower() + '}] }'
    return rpc.rpc_request(data)


def getsnapshot(top=0):
    '''
    The getsnapshot method returns a snapshot of addresses and their amounts at the asset chain's current height.
    The method requires addressindex to be enabled.
    :param top: (number, optional)	Only return this many addresses, i.e. top N rich lis
    :return: JSON string containing:
        "addresses"	(array of jsons)	the array containing the address and amount details
        "addr"	(string)	an address
        "amount"	(number)	the amount of coins in the above address
        "total"	(numeric)	the total amount in snapshot
        "average"	(numeric)	the average amount in each address
        "utxos"	(number)	the total number of UTXOs in snapshot
        "total_addresses"	(number)	the total number of addresses in snapshot,
        "start_height"	(number)	the block height snapshot began
        "ending_height"	(number)	the block height snapshot finished,
        "start_time"	(number)	the unix epoch time snapshot started
        "end_time"	(number)	the unix epoch time snapshot finished
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "getsnapshot", "params": ["' + str(top) + '"] }'
    return rpc.rpc_request(data)