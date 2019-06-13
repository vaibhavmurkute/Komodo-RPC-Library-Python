import rpc_util.rpc as rpc

# node: ip:port
# command: 'add' to add a node to the list, 'remove' to remove a node from the list, 'onetry' to try a connection to the node once
def addnode(node='', command=''):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "addnode", "params": ["' + str(node) + '", "' + str(command) + '"] }'
    return rpc.rpc_request(data)


def clearbanned():
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "clearbanned", "params": [] }'
    return rpc.rpc_request(data)


def disconnectnode(node=''):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "disconnectnode", "params": ["' + str(node) + '"] }'
    return rpc.rpc_request(data)


# Nodes added via onetry are not listed here.
def getaddednodeinfo(dns=False, node=''):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "getaddednodeinfo", "params": [' + str(
        dns).lower() + ', "' + str(node) + '"] }'
    return rpc.rpc_request(data)


def getconnectioncount():
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "getconnectioncount", "params": [] }'
    return rpc.rpc_request(data)


# This method is applicable only to the KMD main net.
def getdeprecationinfo():
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "getdeprecationinfo", "params": [] }'
    return rpc.rpc_request(data)


def getnettotals():
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "getnettotals", "params": [] }'
    return rpc.rpc_request(data)


def getnetworkinfo():
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "getnetworkinfo", "params": [] }'
    return rpc.rpc_request(data)


def getpeerinfo():
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "getpeerinfo", "params": [] }'
    return rpc.rpc_request(data)


def listbanned():
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "listbanned", "params": [] }'
    return rpc.rpc_request(data)


def ping():
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "ping", "params": [] }'
    return rpc.rpc_request(data)


# argument ip(/netmask): the IP/subnet (see getpeerinfo for nodes ip) with an optional netmask (default is /32 = single ip)
# command: use "add" to add an IP/subnet to the list, or "remove" to remove an IP/subnet from the list
# bantime: indicates how long (in seconds) the ip is banned (or until when, if [absolute] is set). 0 or empty means the ban is using the default time of 24h, which can also be overwritten using the -bantime runtime parameter.
# absolute: if set to true, the bantime must be an absolute timestamp (in seconds) since epoch (Jan 1 1970 GMT)
def setban(ip='', command='', bantime=0, absolute=False):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "setban", "params": ["' + str(ip) + '", "' + str(command) + '", ' + str(bantime) + ', ' + str(absolute).lower() + '] }'
    return rpc.rpc_request(data)