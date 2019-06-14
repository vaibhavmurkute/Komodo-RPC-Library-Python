import rpc_util.rpc as rpc

def createmultisig(number_required=1, keys=['']):
    key_list = "[";
    for addr in keys:
        # it seems Komodo rpc considers ' and " differently.. so instead of just str(keys), have to do this
        key_list += "\"" + str(addr) + "\","
    if (len(keys) > 0):
        key_list = key_list[:-1]
    key_list += "]";
    data = '{'+rpc.get_request_metadata()+', "method": "createmultisig", "params": [' + str(
        number_required) + ', ' + str(key_list) + '] }'
    return rpc.rpc_request(data)


def decodeccopret(scriptPubKey=''):
    data = '{'+rpc.get_request_metadata()+', "method": "decodeccopret", "params": ["' + scriptPubKey + '"] }'
    return rpc.rpc_request(data)


# The value -1.0 is returned if not enough transactions and blocks have been observed to make an estimate
def estimatefee(num_blocks=0):
    data = '{'+rpc.get_request_metadata()+', "method": "estimatefee", "params": [' + str(num_blocks) + '] }'
    return rpc.rpc_request(data)


# The value -1.0 is returned if not enough transactions and blocks have been observed to make an estimate
def estimatepriority(num_blocks=0):
    data = '{'+rpc.get_request_metadata()+', "method": "estimatepriority", "params": [' + str(num_blocks) + '] }'
    return rpc.rpc_request(data)


def invalidateblock(block_hash=''):
    data = '{'+rpc.get_request_metadata()+', "method": "invalidateblock", "params": ["' + str(block_hash) + '"] }'
    return rpc.rpc_request(data)


def reconsiderblock(block_hash=''):
    data = '{'+rpc.get_request_metadata()+', "method": "reconsiderblock", "params": ["' + str(block_hash) + '"] }'
    return rpc.rpc_request(data)


def txnotarizedconfirmed(tx_id=''):
    data = '{'+rpc.get_request_metadata()+', "method": "txnotarizedconfirmed", "params": ["' + str(tx_id) + '"] }'
    return rpc.rpc_request(data)


def validateaddress(address=''):
    data = '{'+rpc.get_request_metadata()+', "method": "validateaddress", "params": ["' + str(address) + '"] }'
    return rpc.rpc_request(data)


def verifymessage(address='', signature='', message=''):
    data = '{'+rpc.get_request_metadata()+', "method": "verifymessage", "params": ["' + str(address) + '", "' + str(
        signature) + '", "' + str(message) + '"] }'
    return rpc.rpc_request(data)


def z_validateaddress(address=''):
    data = '{'+rpc.get_request_metadata()+', "method": "z_validateaddress", "params": ["' + str(address) + '"] }'
    return rpc.rpc_request(data)