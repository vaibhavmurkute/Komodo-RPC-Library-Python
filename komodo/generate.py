import rpc_util.rpc as rpc

def generate(numblocks=1):
    '''
    The generate method instructs the coin daemon to immediately mine the indicated number of blocks.
    This function can only be used in the regtest mode (for testing purposes).
    :param numblocks: (numeric)	the desired number of blocks to generate
    :return: blockhashes (JSON string) hashes of blocks generated
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "generate", "params": [' + str(numblocks) + '] }'
    return rpc.rpc_request(data)

def getgenerate():
    '''
    The getgenerate method returns a boolean value indicating the server's mining status.
    :return: true/false (boolean) indicates whether the server is set to generate coins
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "getgenerate", "params": [] }'
    return rpc.rpc_request(data)

def setgenerate(generate=False, genproclimit=2):
    '''
    The setgenerate method allows the user to set the generate property in the coin daemon to true or false, thus turning generation (mining/staking) on or off.
    :param generate: (boolean, required) set to true to turn on generation; set to off to turn off generation
    :param genproclimit: (numeric, optional) set the processor limit for when generation is on; use value "-1" for unlimited
    :return:JSON string
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "setgenerate", "params": ['+str(generate).lower()+', '+str(genproclimit)+'] }'
    return rpc.rpc_request(data)