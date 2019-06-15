import rpc_util.rpc as rpc

def createrawtransaction(transactions={'': 0}, amounts={'',0.0}, memo='', minconf=1, fee=0.0001):
    tx_list = '[';
    for tx_id in transactions:
        tx_list += '{"txid":"' + tx_id + '", "vout": ' + str(transactions[tx_id]) + '},'
    if (len(transactions) > 0):
        tx_list = tx_list[:-1]
    tx_list += ']'
    amount_list = '{';
    for addr in amounts:
        amount_list += '"' + addr + '":' + str(amounts[addr]) + ','
    if (len(amounts) > 0):
        amount_list = amount_list[:-1]
    amount_list += '}'
    data = '{'+rpc.get_request_metadata()+', "method": "createrawtransaction", "params": ['+tx_list+', '+amount_list+(', "'+str(memo)+'"' if memo != '' else '')+(', '+str(minconf) if minconf != 1 else '')+ (', '+str(fee) if fee != 0.0001 else '')+'] }'
    return rpc.rpc_request(data)

def decoderawtransaction(hexstring=''):
    data = '{'+rpc.get_request_metadata()+', "method": "decoderawtransaction", "params": ["' + str(hexstring) + '"] }'
    return rpc.rpc_request(data)

def decodescript(hexstring=''):
    data = '{'+rpc.get_request_metadata()+', "method": "decodescript", "params": ["' + str(hexstring) + '"] }'
    return rpc.rpc_request(data)

def fundrawtransaction(hexstring=''):
    data = '{'+rpc.get_request_metadata()+', "method": "fundrawtransaction", "params": ["' + str(hexstring) + '"] }'
    return rpc.rpc_request(data)

def getrawtransaction(txid='', verbose=0):
    data = '{'+rpc.get_request_metadata()+', "method": "getrawtransaction", "params": ["' + str(txid) + '", '+str(verbose)+'] }'
    return rpc.rpc_request(data)

def sendrawtransaction(hexstring='', allowhighfees=False):
    data = '{'+rpc.get_request_metadata()+', "method": "sendrawtransaction", "params": ["' + str(hexstring) + '", '+str(allowhighfees).lower()+'] }'
    return rpc.rpc_request(data)

def signrawtransaction(hexstring=''):
    data = '{'+rpc.get_request_metadata()+', "method": "signrawtransaction", "params": ["' + str(hexstring) + '" ] }'
    return rpc.rpc_request(data)

