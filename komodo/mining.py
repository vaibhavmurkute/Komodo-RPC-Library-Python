import rpc_util.rpc as rpc

def getblocksubsidy(height=0):
    '''
    The getblocksubsidy method returns the block-subsidy reward.
    :param height: (numeric, optional) the block height; if the block height is not provided, the method defaults to the current height of the chain
    :return: "miner" (numeric) the mining reward amount
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "getblocksubsidy", "params": [' + (str(height) if height > 0 else '') + '] }'
    return rpc.rpc_request(data)


def getblocktemplate(mode='', capabilities=[''], support=''):
    '''
    The getblocktemplate method returns data that is necessary to construct a block.
    :param mode: (string, optional)	this must be set to "template" or omitted
    :param capabilities: [string, optional] a list of capability strings
    :param support: (string) client side supported features: "longpoll", "coinbasetxn", "coinbasevalue", "proposal", "serverlist", "workid"
    :return: JSON string with details necessary to construct a block.
    '''
    cap_list = '[';
    for cap in capabilities:
        cap_list += '"' + cap + '",'
    if (len(capabilities) > 0):
        cap_list = cap_list[:-1]
    cap_list += ']'
    data = '{'+rpc.get_request_metadata()+', "method": "getblocktemplate", "params": [{' + ('"mode":"'+str(mode)+'",' if mode != '' else '')+('"capabilities:"'+cap_list if (len(capabilities) > 0 and capabilities[0] != '') else '') + ('"support":"'+support+'"' if support != '' else '') + '}] }'
    return rpc.rpc_request(data)

def getlocalsolps():
    '''
    The getlocalsolps method returns the average local solutions per second since this node was started.
    :return: "data" (numeric) the solutions-per-second average
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "getlocalsolps", "params": [] }'
    return rpc.rpc_request(data)

def getmininginfo():
    '''
    The getmininginfo method returns a json object containing mining-related information.
    :return: JSON string with mining-related information.
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "getmininginfo", "params": [] }'
    return rpc.rpc_request(data)

def getnetworksolps(blocks=120, height=-1):
    '''
    The getnetworksolps method returns the estimated network solutions per second based on the last n blocks.
    :param blocks: (numeric, optional, default=120)	the number of blocks; use -1 to calculate according to the relevant difficulty averaging window
    :param height: (numeric, optional, default=-1)	the block height that corresponds to the requested data
    :return: data (numeric)	solutions per second, estimated
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "getnetworksolps", "params": ['+str(blocks)+', '+str(height)+'] }'
    return rpc.rpc_request(data)

def prioritisetransaction(txid='', priority_delta=0.0, fee_delta=0):
    '''
    The prioritisetransaction method instructs the daemon to accept the indicated transaction into mined blocks at a higher (or lower) priority.
    :param txid: (string, required)	the transaction id
    :param priority_delta: (numeric, required) the priority to add or subtract (if negative).
    :param fee_delta: (numeric, required) the fee value in satoshis to add or subtract (if negative);
    :return: true	(JSON string)	returns true
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "prioritisetransaction", "params": ["'+str(txid)+'", '+str(priority_delta)+', '+str(fee_delta)+'] }'
    return rpc.rpc_request(data)

def submitblock(hexdata='', workid=''):
    '''
    The submitblock method instructs the daemon to propose a new block to the network.
    :param hexdata: (string, required)	the hex-encoded block data to submit.
    :param workid: (string, sometimes optional)	if the server provides a workid, it MUST be included with submissions
    :return: JSON string containing:
        "duplicate"		            the node already has a valid copy of the block
        "duplicate-invalid"		    the node already has the block, but it is invalid
        "duplicate-inconclusive"    the node already has the block but has not validated it
        "inconclusive"		        the node has not validated the block, it may not be on the node's current best chain
        "rejected"		            the block was rejected as invalid
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "submitblock", "params": ["'+str(hexdata)+'"'+(', "'+str(workid)+'"' if workid != '' else '')+'] }'
    return rpc.rpc_request(data)

