import rpc_util.rpc as rpc

def getinfo():
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "getinfo", "params": [] }'
    return rpc.rpc_request(data)


def help(command=''):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "help", "params": ["' + str(command) + '"] }'
    return rpc.rpc_request(data)


def stop(command=''):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "stop", "params": [] }'
    return rpc.rpc_request(data)