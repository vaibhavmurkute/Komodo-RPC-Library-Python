import requests
from komodo_rpc import KomodoRpc

jsonrpc_ver = '1.0'
rpc_req_id = 'curltest'

def rpc_request(data_string=''):
    response = requests.post(KomodoRpc.req_url, headers=KomodoRpc.req_headers, data=data_string,
                             auth=(KomodoRpc.rpc_username, KomodoRpc.rpc_password))
    if (response.ok):
        return response.text
    else:
        return 'Failed with Status Code: ' + str(response.status_code) + ', reason: ' + str(response.reason)

def get_request_metadata():
    return '"jsonrpc": "'+str(jsonrpc_ver)+'", "id":"'+str(rpc_req_id)+'"'


