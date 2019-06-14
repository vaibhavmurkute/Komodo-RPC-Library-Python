import rpc_util.rpc as rpc

def getinfo():
    data = '{'+rpc.get_request_metadata()+', "method": "getinfo", "params": [] }'
    return rpc.rpc_request(data)


def help(command=''):
    data = '{'+rpc.get_request_metadata()+', "method": "help", "params": ["' + str(command) + '"] }'
    return rpc.rpc_request(data)


def stop(command=''):
    data = '{'+rpc.get_request_metadata()+', "method": "stop", "params": [] }'
    return rpc.rpc_request(data)