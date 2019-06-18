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
    req_url = 'http://' + str(node_addr) + ':' + str(rpc_port) + '/';
    req_headers = {
        'content-type': 'text/plain;'
    }

    def __new__(cls, node_addr='127.0.0.1', rpc_port=7777, req_method='POST', rpc_username='', rpc_password=''):
        cls.node_addr = node_addr
        cls.rpc_port = rpc_port
        cls.req_method = req_method
        cls.rpc_username = rpc_username
        cls.rpc_password = rpc_password
        cls.req_auth = {
            'user': rpc_username,
            'pass': rpc_password
        }
        cls.req_url = 'http://'+str(cls.node_addr)+':'+str(cls.rpc_port)+'/';
        cls.req_headers = {
            'content-type': 'text/plain;'
        }
