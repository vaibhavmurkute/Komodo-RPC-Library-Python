import rpc_util.rpc as rpc

def getinfo():
    '''
    The getinfo method returns an object containing various state info
    :return: JSON string conataining wallet state and network state info
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "getinfo", ' \
                '"params": [] }'
    return rpc.rpc_request(data)


def help(command=''):
    '''
    The help method lists all commands, or all information
    for a specified command
    :param command: (string, optional) the command requiring assistance
    :return: "help"	(JSON string) the command requiring assistance
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "help", ' \
                '"params": ["' + str(command) + '"] }'
    return rpc.rpc_request(data)


def stop():
    '''
    The stop method instructs the coin daemon to shut down.
    :return: JSON string: Komodo server stopping
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "stop", ' \
                '"params": [] }'
    return rpc.rpc_request(data)