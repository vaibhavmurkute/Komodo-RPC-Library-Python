class KomodoRpc:
    node_addr = '127.0.0.1'
    rpc_port = 7777
    req_method = 'POST'
    rpc_username = ''
    rpc_password = ''
    req_auth = {
        'user': rpc_username,
        'pass': rpc_password
    }
    req_url = 'http://{0}:{1}/'.format(str(node_addr), str(rpc_port))
    req_headers = {
        'content-type': 'text/plain;'
    }
    jsonrpc_ver = '1.0'
    rpc_req_id = 'curltest'

    def __new__(cls, node_addr='127.0.0.1', rpc_port=7777, req_method='POST',
                rpc_username='', rpc_password='', jsonrpc_ver = '1.0',
                rpc_req_id = 'curltest'):
        '''
        Create an instance of KomodoRpc class to populate RPC-request options
        and authentication parameters.
        :param node_addr: (string, default='127.0.0.1') IP address of node
            where komodod is listening for RPCs.
        :param rpc_port: (numeric) RPC-Port of running asset-chain
        :param req_method: (string, default='POST') HTTP request method
        :param rpc_username: (string) Username for RPC authentication
        :param rpc_password: (string) Password for RPC authentication
        :param jsonrpc_ver: (string, default='1.0') JSON RPC version
        :param rpc_req_id: (string) ID for RPC requests
        :return: Object of KomodoRpc class
        '''
        cls.node_addr = node_addr
        cls.rpc_port = rpc_port
        cls.req_method = req_method
        cls.rpc_username = rpc_username
        cls.rpc_password = rpc_password
        cls.req_auth = {
            'user': rpc_username,
            'pass': rpc_password
        }
        cls.req_url = 'http://{0}:{1}/'.format(str(cls.node_addr),
                                               str(cls.rpc_port))
        cls.req_headers = {
            'content-type': 'text/plain;'
        }
        cls.jsonrpc_ver = jsonrpc_ver
        cls.rpc_req_id = rpc_req_id

