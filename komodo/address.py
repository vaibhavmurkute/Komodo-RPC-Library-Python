import rpc_util.rpc as rpc

def getaddressbalance(addresses=[""]):
    addr_list = "["
    for addr in addresses:
        addr_list += "\"" + str(addr) + "\","
    if (len(addresses) > 0):
        addr_list = addr_list[:-1]
    addr_list += "]"
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "getaddressbalance", "params": [{"addresses": ' + str(
        addr_list) + '}] }'
    return rpc.rpc_request(data)


def getaddressdeltas(addresses=[""], start=0, end=0, chainInfo=False):
    addr_list = "["
    for addr in addresses:
        addr_list += "\"" + str(addr) + "\","
    if (len(addresses) > 0):
        addr_list = addr_list[:-1]
    addr_list += "]"
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "getaddressdeltas", "params": [{"addresses": ' + str(
        addr_list) + ',"start":' + str(start) + ',"end":' + str(end) + ',"chainInfo":' + str(chainInfo).lower() + '}]}'
    return rpc.rpc_request(data)


def getaddressmempool(addresses=[""]):
    addr_list = "["
    for addr in addresses:
        addr_list += "\"" + str(addr) + "\","
    if (len(addresses) > 0):
        addr_list = addr_list[:-1]
    addr_list += "]"
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "getaddressmempool", "params": [{"addresses": ' + str(
        addr_list) + '}] }'
    return rpc.rpc_request(data)


def getaddresstxids(addresses=[""], start=0, end=0):
    addr_list = "["
    for addr in addresses:
        addr_list += "\"" + str(addr) + "\","
    if (len(addresses) > 0):
        addr_list = addr_list[:-1]
    addr_list += "]"
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "getaddresstxids", "params": [{"addresses": ' + str(
        addr_list) + ', "start":' + str(start) + ',"end":' + str(end) + '}] }'
    return rpc.rpc_request(data)


def getaddressutxos(addresses=[""], chainInfo=False):
    addr_list = "["
    for addr in addresses:
        addr_list += "\"" + str(addr) + "\","
    if (len(addresses) > 0):
        addr_list = addr_list[:-1]
    addr_list += "]"
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "getaddressutxos", "params": [{"addresses": ' + str(
        addr_list) + ', "chainInfo": ' + str(chainInfo).lower() + '}] }'
    return rpc.rpc_request(data)


def getsnapshot(top=0):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "getsnapshot", "params": ["' + str(top) + '"] }'
    return rpc.rpc_request(data)