import rpc_util.rpc as rpc

def z_getpaymentdisclosure(txid='', js_index='', output_index='', message=''):
    '''
    The z_getpaymentdisclosure method generates a payment disclosure for a given joinsplit output
    EXPERIMENTAL FEATURE: Payment disclosure is currently DISABLED. This call always fails.
    :param txid: (string, required)
    :param js_index: (string, required)
    :param output_index: (string, required)
    :param message: (string, optional)
    :return: "paymentdisclosure"	(string)	a hex data string, with a "zpd:" prefix
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "z_getpaymentdisclosure", "params": ["'+str(txid)+'","'+str(js_index)+'","'+str(output_index)+'","'+str(message)+'"] }'
    return rpc.rpc_request(data)


def z_validatepaymentdisclosure(paymentdisclosure=''):
    '''
    The z_validatepaymentdisclosure method validates a payment disclosure.
    :param paymentdisclosure: (string, required)	hex data string, with "zpd:" prefix
    :return: (currently disabled)
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "z_validatepaymentdisclosure", "params": ["'+str(paymentdisclosure)+'"] }'
    return rpc.rpc_request(data)



