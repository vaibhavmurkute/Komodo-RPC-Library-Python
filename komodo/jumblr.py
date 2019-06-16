import rpc_util.rpc as rpc

'''
    The jumblr_deposit method indicates the address from which Jumblr should withdraw funds.
    There should be at least 10.024 KMD in this address
        Arguments:
            - depositaddress  : (string, required) : the address from which Jumblr will withdraw funds
        Response:
            (none)
'''
def jumblr_deposit(depositaddress=''):
    data = '{'+rpc.get_request_metadata()+', "method": "jumblr_deposit", "params": ["'+str(depositaddress)+'"] }'
    return rpc.rpc_request(data)

'''
    The jumblr_pause method instructs Jumblr to temporarily pause the privacy-shielding process.
        Arguments:
            (none)
        Response:
            (none)
'''
def jumblr_pause():
    data = '{'+rpc.get_request_metadata()+', "method": "jumblr_pause", "params": [] }'
    return rpc.rpc_request(data)

'''
    The jumblr_resume method instructs Jumblr to resume the privacy-shielding process.
        Arguments:
            (none)
        Response:
            (none)
'''
def jumblr_resume():
    data = '{'+rpc.get_request_metadata()+', "method": "jumblr_resume", "params": [] }'
    return rpc.rpc_request(data)

'''
    The jumblr_secret method indicates to Jumblr the final t destination address.
        Arguments:
            - secretaddress  : (string, required) : the destination transparent address
        Response:
            (none)
'''
def jumblr_secret(secretaddress=''):
    data = '{'+rpc.get_request_metadata()+', "method": "jumblr_secret", "params": ["'+str(secretaddress)+'"] }'
    return rpc.rpc_request(data)

