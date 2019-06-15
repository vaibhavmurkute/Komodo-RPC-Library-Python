import rpc_util.rpc as rpc

def generate(numblocks=1):
    data = '{'+rpc.get_request_metadata()+', "method": "generate", "params": [' + str(numblocks) + '] }'
    return rpc.rpc_request(data)

def getgenerate():
    data = '{'+rpc.get_request_metadata()+', "method": "getgenerate", "params": [] }'
    return rpc.rpc_request(data)

def setgenerate(generate=False, genproclimit=2):
    data = '{'+rpc.get_request_metadata()+', "method": "setgenerate", "params": ['+str(generate).lower()+', '+str(genproclimit)+'] }'
    return rpc.rpc_request(data)