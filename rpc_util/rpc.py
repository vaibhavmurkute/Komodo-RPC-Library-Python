import requests
from komodo_rpc import KomodoRpc


def rpc_request(data_string=''):
    if KomodoRpc.rpc_username != '':
        req_url = 'http://{0}:{1}/'.format(str(KomodoRpc.node_addr),
                                           str(KomodoRpc.rpc_port))
        response = requests.post(req_url,
                                 headers=KomodoRpc.req_headers,
                                 data=data_string,
                                 auth=(KomodoRpc.rpc_username,
                                       KomodoRpc.rpc_password)
                                 )
    else:
        return '<!> Please check your RPC authentication credentials.\n' \
                    'Usage: KomodoRpc(node_addr, rpc_port, ' \
                    'req_method, rpc_username, rpc_password, jsonrpc_ver, ' \
                    'rpc_req_id) \n' \
                   '\t node_addr: (string, default="127.0.0.1") IP address ' \
                        'of node where komodod is listening for RPCs.\n' \
                   '\t rpc_port: (numeric) RPC-Port of running ' \
                        'asset-chain.\n' \
                   '\t req_method: (string, default="POST") HTTP request ' \
                        'method\n' \
                   '\t rpc_username: (string) Username for RPC ' \
                        'authentication\n' \
                   '\t rpc_password: (string) Password for RPC ' \
                        'authentication.\n' \
                   '\t jsonrpc_ver: (string, default="1.0") JSON RPC ' \
                        'version.\n' \
                   '\t rpc_req_id: (string) ID for RPC requests.\n'

    if response.ok:
        return response.text
    else:
        return '<!> Failed with Status Code: ' + str(response.status_code) + \
                    ', reason: ' + str(response.text)


def get_request_metadata():
    return '"jsonrpc": "'+str(KomodoRpc.jsonrpc_ver)+'", ' \
                '"id":"'+str(KomodoRpc.rpc_req_id)+'"'

