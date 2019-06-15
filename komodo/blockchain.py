import rpc_util.rpc as rpc

def coinsupply(height=0):
    data = '{'+rpc.get_request_metadata()+', "method": "coinsupply", "params": [' + (str(height) if height > 1 else '') + '] }'
    return rpc.rpc_request(data)

def getbestblockhash():
    data = '{'+rpc.get_request_metadata()+', "method": "getbestblockhash", "params": [] }'
    return rpc.rpc_request(data)

def getbestblockhash():
    data = '{'+rpc.get_request_metadata()+', "method": "getbestblockhash", "params": [] }'
    return rpc.rpc_request(data)

'''
    getblock(block):
    Parameters:
        - block_id: (string or number) : string representing block-hash or number representing block height
        - verbose: (boolean) : true returns a json object, false returns hex-encoded data
'''
def getblock(block_id=1, verbose=True):
    data = '{'+rpc.get_request_metadata()+', "method": "getblock", "params": ["'+str(block_id)+'", '+str(verbose).lower()+'] }'
    return rpc.rpc_request(data)

def getblockchaininfo():
    data = '{'+rpc.get_request_metadata()+', "method": "getblockchaininfo", "params": [] }'
    return rpc.rpc_request(data)

def getblockcount():
    data = '{'+rpc.get_request_metadata()+', "method": "getblockcount", "params": [] }'
    return rpc.rpc_request(data)

def getblockhash(index=1):
    data = '{'+rpc.get_request_metadata()+', "method": "getblockhash", "params": ['+str(index)+'] }'
    return rpc.rpc_request(data)

'''
    getblockhashes(high, low, no_orphans, logical_times):
        - high: (numeric, required, default=0) : the newer block timestamp
        - low: (numeric, required, default=0) : the older block timestamp
        - no_orphans (boolean, required, default=False) : a value of true implies that the method will only include blocks on the main chain
        - logical_times (boolean, required, default=False) : a value of true implies that the method will only include logical timestamps with hashes
'''
def getblockhashes(high=0, low=0, no_orphans=False, logical_times=False):
    options = '{"noOrphans":'+str(no_orphans).lower()+', "logicalTimes":'+str(logical_times).lower()+'}'
    data = '{'+rpc.get_request_metadata()+', "method": "getblockhashes", "params": ['+str(high)+', '+str(low)+', '+options+'] }'
    return rpc.rpc_request(data)

def getblockheader(hash='', verbose=True):
    data = '{'+rpc.get_request_metadata()+', "method": "getblockheader", "params": ["'+str(hash)+'", '+str(verbose).lower()+'] }'
    return rpc.rpc_request(data)

def getchaintips():
    data = '{'+rpc.get_request_metadata()+', "method": "getchaintips", "params": [] }'
    return rpc.rpc_request(data)

'''
    getchaintxstats()
    komodo error code: -32601
    error message: Method not found
'''
def getchaintxstats(nblocks=1, blockhash=''):
    data = '{'+rpc.get_request_metadata()+', "method": "getchaintxstats", "params": ['+str(nblocks)+', "'+str(blockhash)+'"] }'
    return rpc.rpc_request(data)

def getdifficulty():
    data = '{'+rpc.get_request_metadata()+', "method": "getdifficulty", "params": [] }'
    return rpc.rpc_request(data)

'''
    getlastsegidstakes(depth=1):
        - Only applies to ac_staked chains
'''
def getlastsegidstakes(depth=1):
    data = '{'+rpc.get_request_metadata()+', "method": "getlastsegidstakes", "params": ['+str(depth)+'] }'
    return rpc.rpc_request(data)

def getmempoolinfo():
    data = '{'+rpc.get_request_metadata()+', "method": "getmempoolinfo", "params": [] }'
    return rpc.rpc_request(data)

def getrawmempool(verbose=False):
    data = '{'+rpc.get_request_metadata()+', "method": "getrawmempool", "params": ['+str(verbose).lower()+'] }'
    return rpc.rpc_request(data)

def getspentinfo(txid='', index=0):
    options = '{"txid":"'+str(txid).lower()+'", "index":'+str(index)+'}'
    data = '{'+rpc.get_request_metadata()+', "method": "getspentinfo", "params": ['+str(options)+'] }'
    return rpc.rpc_request(data)

def gettxout(txid='', vout=0, includemempool=False):
    data = '{'+rpc.get_request_metadata()+', "method": "gettxout", "params": ["'+str(txid)+'", '+str(vout)+', '+str(includemempool).lower()+'] }'
    return rpc.rpc_request(data)

def gettxoutproof(txid=[''], blockhash=''):
    txid_list = "[";
    for tx in txid:
        txid_list += "\"" + str(tx) + "\","
    if (len(txid) > 0):
        txid_list = txid_list[:-1]
    txid_list += "]";
    data = '{'+rpc.get_request_metadata()+', "method": "gettxoutproof", "params": ['+txid_list+ (', "'+str(blockhash)+'"' if blockhash != '' else '') +'] }'
    return rpc.rpc_request(data)

def gettxoutsetinfo():
    data = '{'+rpc.get_request_metadata()+', "method": "gettxoutsetinfo", "params": [] }'
    return rpc.rpc_request(data)

def kvsearch(key=''):
    data = '{'+rpc.get_request_metadata()+', "method": "kvsearch", "params": ["'+str(key)+'"] }'
    return rpc.rpc_request(data)

def kvupdate(key='', value='', days=1, passphrase=''):
    data = '{'+rpc.get_request_metadata()+', "method": "kvupdate", "params": ["'+str(key)+'","'+str(value)+'","'+str(days)+'", "'+str(passphrase)+'"] }'
    return rpc.rpc_request(data)

def minerids(height=1):
    data = '{'+rpc.get_request_metadata()+', "method": "minerids", "params": ["'+str(height)+'"] }'
    return rpc.rpc_request(data)

def notaries(height=0, timestamp=0):
    options = ('"'+str(height)+'", "'+str(timestamp)+'"' if(height != 0 and timestamp != 0) else('"'+str(height)+'"' if height > 0 else(('"'+str(timestamp)+'"' if timestamp > 0 else ''))))
    data = '{'+rpc.get_request_metadata()+', "method": "notaries", "params": ['+options+'] }'
    return rpc.rpc_request(data)

def verifychain(checklevel=3, numblocks=0):
    data = '{'+rpc.get_request_metadata()+', "method": "verifychain", "params": ['+str(checklevel)+','+str(numblocks)+'] }'
    return rpc.rpc_request(data)

def verifytxoutproof(proofstring=''):
    data = '{'+rpc.get_request_metadata()+', "method": "verifytxoutproof", "params": ["'+str(proofstring)+'"] }'
    return rpc.rpc_request(data)

