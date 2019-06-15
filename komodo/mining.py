import rpc_util.rpc as rpc

def getblocksubsidy(height=0):
    data = '{'+rpc.get_request_metadata()+', "method": "getblocksubsidy", "params": [' + (str(height) if height > 0 else '') + '] }'
    return rpc.rpc_request(data)

def getblocksubsidy(height=0):
    data = '{'+rpc.get_request_metadata()+', "method": "getblocksubsidy", "params": [' + (str(height) if height > 0 else '') + '] }'
    return rpc.rpc_request(data)

def getblocktemplate(mode='', capabilities=[''], support=''):
    cap_list = '[';
    for cap in capabilities:
        cap_list += '"' + cap + '",'
    if (len(capabilities) > 0):
        cap_list = cap_list[:-1]
    cap_list += ']'
    data = '{'+rpc.get_request_metadata()+', "method": "getblocktemplate", "params": [{' + ('"mode":"'+str(mode)+'",' if mode != '' else '')+('"capabilities:"'+cap_list if (len(capabilities) > 0 and capabilities[0] != '') else '') + ('"support":"'+support+'"' if support != '' else '') + '}] }'
    return rpc.rpc_request(data)

def getlocalsolps():
    data = '{'+rpc.get_request_metadata()+', "method": "getlocalsolps", "params": [] }'
    return rpc.rpc_request(data)

def getmininginfo():
    data = '{'+rpc.get_request_metadata()+', "method": "getmininginfo", "params": [] }'
    return rpc.rpc_request(data)

def getnetworksolps(blocks=120, height=-1):
    data = '{'+rpc.get_request_metadata()+', "method": "getnetworksolps", "params": ['+str(blocks)+', '+str(height)+'] }'
    return rpc.rpc_request(data)

def prioritisetransaction(txid='', priority_delta=0.0, fee_delta=0):
    data = '{'+rpc.get_request_metadata()+', "method": "prioritisetransaction", "params": ["'+str(txid)+'", '+str(priority_delta)+', '+str(fee_delta)+'] }'
    return rpc.rpc_request(data)

def submitblock(hexdata='', workid=''):
    data = '{'+rpc.get_request_metadata()+', "method": "submitblock", "params": ["'+str(hexdata)+'"'+(', "'+str(workid)+'"' if workid != '' else '')+'] }'
    return rpc.rpc_request(data)

