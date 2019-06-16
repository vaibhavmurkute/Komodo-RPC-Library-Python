import rpc_util.rpc as rpc

'''
    z_getpaymentdisclosure method generates a payment disclosure for a given joinsplit output.
        Arguments:
            - txid          : (string, required)
            - js_index      :  (string, required)
            - output_index  : (string, required)
            - message       : (string, optional)
        Response:
            - paymentdisclosure : (string) : a hex data string, with a "zpd:" prefix
'''
def z_getpaymentdisclosure(txid='', js_index='', output_index='', message=''):
    data = '{'+rpc.get_request_metadata()+', "method": "z_getpaymentdisclosure", "params": ["'+str(txid)+'","'+str(js_index)+'","'+str(output_index)+'","'+str(message)+'"] }'
    return rpc.rpc_request(data)

'''
    The z_validatepaymentdisclosure method validates a payment disclosure.
        Arguments:
            - paymentdisclosure : (string, required): hex data string, with "zpd:" prefix
        Response:
            (currently disabled)		
'''
def z_validatepaymentdisclosure(paymentdisclosure=''):
    data = '{'+rpc.get_request_metadata()+', "method": "z_validatepaymentdisclosure", "params": ["'+str(paymentdisclosure)+'"] }'
    return rpc.rpc_request(data)



