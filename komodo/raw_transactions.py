import rpc_util.rpc as rpc

def createrawtransaction(transactions={'': 0}, amounts={'',0.0}):
    '''
    The createrawtransaction method creates a transaction, spending the given inputs and sending to the given addresses.
    :param transactions: {string, number} a dictinary of txid (string) as key and vout (number) as value.
    :param amounts: {string, number} a dictinary of address (string) as key and amount (number) as value.
    :return: "transaction"	(JSON string) a hex string of the transaction
    '''
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
    data = '{'+rpc.get_request_metadata()+', "method": "createrawtransaction", "params": ['+tx_list+', '+amount_list+'] }'
    return rpc.rpc_request(data)

def decoderawtransaction(hexstring=''):
    '''
    The decoderawtransaction method returns a json object representing the serialized, hex-encoded transaction.
    :param hexstring: (string, required) the transaction hex string.
    :return: JSON string with the serialized, hex-encoded transaction.
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "decoderawtransaction", "params": ["' + str(hexstring) + '"] }'
    return rpc.rpc_request(data)

def decodescript(hexstring=''):
    '''
    The decodescript method decodes a hex-encoded script.
    :param hexstring: (string)	the hex encoded script
    :return: JSON string containing:
        "asm"	        (string)	the script public key
        "hex"	        (string)	the hex-encoded public key
        "type"	        (string)	the output type
        "reqSigs"	    (numeric)	the required signatures
        "addresses":    [ ... ]	    (array of strings)
        "address"	    (string)	the address
        "p2sh"	        (string)	the script address
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "decodescript", "params": ["' + str(hexstring) + '"] }'
    return rpc.rpc_request(data)

def fundrawtransaction(hexstring=''):
    '''
    The fundrawtransaction method adds inputs to a transaction until it has enough in value to meet its out value.
    :param hexstring: (string, required) the hex string of the raw transaction
    :return: JSON string containing:
        "hex"	    (string)	the resulting raw transaction (hex-encoded string)
        "fee"	    (numeric)	the fee added to the transaction
        "changepos"	(numeric)	the position of the added change output, or -1
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "fundrawtransaction", "params": ["' + str(hexstring) + '"] }'
    return rpc.rpc_request(data)

def getrawtransaction(txid='', verbose=0):
    '''
    The getrawtransaction method returns the raw transaction data.
    :param txid: (string, required)	the transaction id
    :param verbose: (numeric, optional, default=0)	if 0, the method returns a string in hex; otherwise, it returns a json object
    :return: "data"	(JSON string) if verbose is not set, or set to 0, the serialized, hex-encoded data for 'txid'
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "getrawtransaction", "params": ["' + str(txid) + '", '+str(verbose)+'] }'
    return rpc.rpc_request(data)

def sendrawtransaction(hexstring='', allowhighfees=False):
    '''
    The sendrawtransction method submits raw transaction (serialized, hex-encoded) to local nodes and the network.
    :param hexstring: (string, required) the hex string of the raw transaction
    :param allowhighfees: (boolean, optional, default=false) whether to allow high fees
    :return: "hex" (JSON string) the transaction hash in hex
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "sendrawtransaction", "params": ["' + str(hexstring) + '", '+str(allowhighfees).lower()+'] }'
    return rpc.rpc_request(data)

def signrawtransaction(hexstring=''):
    '''
    The signrawtransaction method signs inputs for a raw transaction (serialized, hex-encoded).
    :param hexstring: (string, required) the transaction hex string
    :return: JSON string containing:
        "hex"	    (string)	the hex-encoded raw transaction with signature(s)
        "complete"	(boolean)	whether the transaction has a complete set of signatures
        "errors"
        "txid"	    (string)	the hash of the referenced, previous transaction
        "vout"	    (numeric)	the index of the output to spend and used as input
        "scriptSig"	(string)	the hex-encoded signature script
        "sequence"	(numeric)	the script sequence number
        "error"	    (string)	verification or signing error related to the input
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "signrawtransaction", "params": ["' + str(hexstring) + '" ] }'
    return rpc.rpc_request(data)

