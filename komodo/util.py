import rpc_util.rpc as rpc

def createmultisig(number_required=1, keys=['']):
    key_list = "[";
    for addr in keys:
        # it seems Komodo rpc considers ' and " differently.. so instead of just str(keys), have to do this
        key_list += "\"" + str(addr) + "\","
    if (len(keys) > 0):
        key_list = key_list[:-1]
    key_list += "]";
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "createmultisig", "params": [' + str(
        number_required) + ', ' + str(key_list) + '] }'
    return rpc.rpc_request(data)


def decodeccopret(scriptPubKey=''):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "decodeccopret", "params": ["' + scriptPubKey + '"] }'
    return rpc.rpc_request(data)


# The value -1.0 is returned if not enough transactions and blocks have been observed to make an estimate
def estimatefee(num_blocks=0):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "estimatefee", "params": [' + str(num_blocks) + '] }'
    return rpc.rpc_request(data)


# The value -1.0 is returned if not enough transactions and blocks have been observed to make an estimate
def estimatepriority(num_blocks=0):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "estimatepriority", "params": [' + str(num_blocks) + '] }'
    return rpc.rpc_request(data)


def invalidateblock(block_hash=''):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "invalidateblock", "params": ["' + str(block_hash) + '"] }'
    return rpc.rpc_request(data)


def reconsiderblock(block_hash=''):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "reconsiderblock", "params": ["' + str(block_hash) + '"] }'
    return rpc.rpc_request(data)


def txnotarizedconfirmed(tx_id=''):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "txnotarizedconfirmed", "params": ["' + str(tx_id) + '"] }'
    return rpc.rpc_request(data)


def validateaddress(address=''):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "validateaddress", "params": ["' + str(address) + '"] }'
    return rpc.rpc_request(data)


def verifymessage(address='', signature='', message=''):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "verifymessage", "params": ["' + str(address) + '", "' + str(
        signature) + '", "' + str(message) + '"] }'
    return rpc.rpc_request(data)


def z_validateaddress(address=''):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "z_validateaddress", "params": ["' + str(address) + '"] }'
    return rpc.rpc_request(data)