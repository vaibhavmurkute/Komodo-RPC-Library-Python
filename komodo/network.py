import rpc_util.rpc as rpc

def addnode(node='', command=''):
    '''
    The addnode method attempts to add or remove a node from the addnode list, or to make a single attempt to connect to a node.
    :param node: (string, required) node_ip:port
    :param command: (string, required) 'add' to add a node to the list, 'remove' to remove a node from the list, 'onetry' to try a connection to the node once
    :return: JSON string
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "addnode", "params": ["' + str(node) + '", "' + str(command) + '"] }'
    return rpc.rpc_request(data)


def clearbanned():
    '''
    The clearbanned method clears all banned IPs
    :return: JSON string
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "clearbanned", "params": [] }'
    return rpc.rpc_request(data)


def disconnectnode(node=''):
    '''
    The disconnectnode method instructs the daemon to immediately disconnect from the specified node.
    :param node: (string, required) node_ip:port
    :return: JSON string
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "disconnectnode", "params": ["' + str(node) + '"] }'
    return rpc.rpc_request(data)


def getaddednodeinfo(dns=False, node=''):
    '''
    The getaddednodeinfo method returns information about the given added node, or all added nodes.
    Nodes added via onetry are not listed here.
    :param dns: (boolean, required)	if false, only a list of added nodes will be provided; otherwise, connection information is also provided
    :param node: (string, optional)	if provided, the method returns information about this specific node; otherwise, all nodes are returned
    :return: JSON string containing:
        "addednode"	    (string)	the node ip address
        "connected"	    (boolean)	if connected
        "addresses"     [ ... ]	    (array of jsons)
        "address"	    (string)	the server host and port
        "connected"	    (string)	"connected" accepts two possible values: "inbound" or "outbound"
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "getaddednodeinfo", "params": [' + str(
        dns).lower() + ', "' + str(node) + '"] }'
    return rpc.rpc_request(data)


def getconnectioncount():
    '''
    The getconnectioncount method returns the number of connections to other nodes.
    :return: n (numeric) the connection count
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "getconnectioncount", "params": [] }'
    return rpc.rpc_request(data)


def getdeprecationinfo():
    '''
    The getdeprecationinfo method returns an object containing current version and deprecation block height.
    This method is applicable only to the KMD main net
    :return: JSON string containing:
        "version"	        (numeric)	the server version
        "subversion"	    (string)	the server sub-version string (i.e. "/MagicBean:x.y.z[-v]/")
        "deprecationheight"	(numeric)	the block height at which this version will deprecate and shut down
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "getdeprecationinfo", "params": [] }'
    return rpc.rpc_request(data)


def getnettotals():
    '''
    The getnettotals method returns information about network traffic, including bytes in, bytes out, and current time.
    :return: JSON string containing:
        "totalbytesrecv"	(numeric)	total bytes received
        "totalbytessent"	(numeric)	total bytes sent
        "timemillis"	    (numeric)	total cpu time
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "getnettotals", "params": [] }'
    return rpc.rpc_request(data)


def getnetworkinfo():
    '''
    The getnetworkinfo method returns an object containing various state info regarding p2p networking.
    :return: JSON string with various state info regarding p2p networking.
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "getnetworkinfo", "params": [] }'
    return rpc.rpc_request(data)


def getpeerinfo():
    '''
    The getpeerinfo method returns data about each connected network node as a json array of objects.
    :return: JSON string with data about each connected network node as a json array of objects.
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "getpeerinfo", "params": [] }'
    return rpc.rpc_request(data)


def listbanned():
    '''
    The listbanned method lists all banned IP addresses and subnets
    :return: JSON string containing:
        "address"	    (string)	the address/subnet that is banned
        "banned_until"	(numeric)	the timestamp, at which point the ban will be removed
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "listbanned", "params": [] }'
    return rpc.rpc_request(data)


def ping():
    '''
    The ping method requests that a ping be sent to all other nodes, to measure ping time.
    :return: JSON string
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "ping", "params": [] }'
    return rpc.rpc_request(data)


def setban(ip='', command='', bantime=0, absolute=False):
    '''
    The setban method attempts to add or remove an IP address (and subnet, if indicated) from the banned list
    :param ip: (string, ip required) the IP/subnet with an optional netmask (default is /32 = single ip)
    :param command: (string, required)	use "add" to add an IP/subnet to the list, or "remove" to remove an IP/subnet from the list
    :param bantime: (numeric, optional)	indicates how long (in seconds) the ip is banned (or until when, if [absolute] is set). 0 or empty means the ban is using the default time of 24h.
    :param absolute: (boolean, optional) if set to true, the bantime must be an absolute timestamp (in seconds) since epoch (Jan 1 1970 GMT)
    :return: JSON string
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "setban", "params": ["' + str(ip) + '", "' + str(command) + '", ' + str(bantime) + ', ' + str(absolute).lower() + '] }'
    return rpc.rpc_request(data)