import rpc_util.rpc as rpc


def jumblr_deposit(depositaddress=''):
    '''
    The jumblr_deposit method indicates the address from which
    Jumblr should withdraw funds.
    :param depositaddress: (string, required) the address from
        which Jumblr will withdraw funds
    :return: JSON string
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "jumblr_deposit", ' \
                '"params": ["'+str(depositaddress)+'"] }'
    return rpc.rpc_request(data)


def jumblr_pause():
    '''
    The jumblr_pause method instructs Jumblr to temporarily pause
    the privacy-shielding process.
    :return: JSON string
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "jumblr_pause", ' \
                '"params": [] }'
    return rpc.rpc_request(data)


def jumblr_resume():
    '''
    The jumblr_resume method instructs Jumblr to resume
    the privacy-shielding process.
    :return: JSON string
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "jumblr_resume", ' \
                '"params": [] }'
    return rpc.rpc_request(data)


def jumblr_secret(secretaddress=''):
    '''
    The jumblr_secret method indicates to Jumblr the final
    t destination address.
    :param secretaddress: (string, required) the destination
        transparent address
    :return: JSON string
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "jumblr_secret", ' \
                '"params": ["'+str(secretaddress)+'"] }'
    return rpc.rpc_request(data)



