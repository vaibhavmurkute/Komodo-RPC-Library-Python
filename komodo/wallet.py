import rpc_util.rpc as rpc

def getwalletinfo():
    # id field need to be updated
    data = '{'+rpc.get_request_metadata()+', "method": "getwalletinfo", "params": [] }'
    return rpc.rpc_request(data)

def backupwallet(filename):
    '''
        This method requires that the coin daemon have the 'exportdir' runtime parameter enabled.
        exportdir tells the coin daemon where to store the komodo backup files created through the backupwallet and dumpwallet calls.
        Parameters: the 'destination' filename, saved in the directory set by the exportdir runtime parameter
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "backupwallet", "params": ["' + str(filename) + '"] }'
    return rpc.rpc_request(data)

def dumpprivkey(address):
    data = '{'+rpc.get_request_metadata()+', "method": "dumpprivkey", "params": ["' + str(address) + '"] }'
    return rpc.rpc_request(data)

def dumpwallet(filename):
    '''
    This method requires that the coin daemon have the 'exportdir' runtime parameter enabled.
    exportdir tells the coin daemon where to store the komodo backup files created through the backupwallet and dumpwallet calls.
    Parameters: the 'destination' filename, saved in the directory set by the exportdir runtime parameter
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "dumpwallet", "params": ["' + str(filename) + '"] }'
    return rpc.rpc_request(data)

def getaccount(address):
    data = '{'+rpc.get_request_metadata()+', "method": "getaccount", "params": ["' + str(address) + '"] }'
    return rpc.rpc_request(data)

# getbalance with account is deprecated
def getbalance(account='', minconf=1, includeWatchOnly=False):
    data = '{'+rpc.get_request_metadata()+', "method": "getbalance", "params": ["",1] }'
    return rpc.rpc_request(data)

# getnewaddress with account is deprecated
def getnewaddress(account=''):
    data = '{'+rpc.get_request_metadata()+', "method": "getnewaddress", "params": [] }'
    return rpc.rpc_request(data)

# This is for use with raw transactions, NOT normal use.
def getrawchangeaddress():
    data = '{'+rpc.get_request_metadata()+', "method": "getrawchangeaddress", "params": [] }'
    return rpc.rpc_request(data)

def getreceivedbyaddress(address, minconf=1):
    data = '{'+rpc.get_request_metadata()+', "method": "getreceivedbyaddress", "params": ["' + str(
        address) + '", ' + str(minconf) + '] }'
    return rpc.rpc_request(data)

def gettransaction(txid, includeWatchOnly=False):
    data = '{'+rpc.get_request_metadata()+', "method": "gettransaction", "params": ["' + str(txid) + ', ' + str(
        includeWatchOnly) + '"] }'
    return rpc.rpc_request(data)

def getunconfirmedbalance():
    data = '{'+rpc.get_request_metadata()+', "method": "getunconfirmedbalance", "params": [] }'
    return rpc.rpc_request(data)

# This call can take an increased amount of time to complete if rescan is true.
def importaddress(address, label='', rescan=True):
    data = '{'+rpc.get_request_metadata()+', "method": "importaddress", "params": ["' + str(address) + '", "' + str(
        label) + '", ' + str(rescan).lower() + '] }'
    return rpc.rpc_request(data)

# This call can take an increased amount of time to complete if rescan is true.
def importprivkey(privKey, label='', rescan=True):
    data = '{'+rpc.get_request_metadata()+', "method": "importprivkey", "params": ["UwibHKsYfiM19BXQmcUwAfw331GzGQK8aoPqqYEbyoPrzc2965nE", "testing", false] }'
    return rpc.rpc_request(data)

def importwallet(path):
    data = '{'+rpc.get_request_metadata()+', "method": "importwallet", "params": ["' + str(path) + '"] }'
    return rpc.rpc_request(data)

def keypoolrefill(newsize=100):
    data = '{'+rpc.get_request_metadata()+', "method": "keypoolrefill", "params": [' + str(newsize) + '] }'
    return rpc.rpc_request(data)

def listaddressgroupings():
    data = '{'+rpc.get_request_metadata()+', "method": "listaddressgroupings", "params": [] }'
    return rpc.rpc_request(data)

# See the lockunspent call to lock and unlock transactions for spending.
def listlockunspent():
    data = '{'+rpc.get_request_metadata()+', "method": "listlockunspent", "params": [] }'
    return rpc.rpc_request(data)

def listreceivedbyaddress(minconf=1, includeEmpty=False, includeWatchOnly=False):
    data = '{'+rpc.get_request_metadata()+', "method": "listreceivedbyaddress", "params": [' + str(
        minconf) + ', ' + str(includeEmpty).lower() + ', ' + str(includeWatchOnly).lower() + '] }'
    return rpc.rpc_request(data)


def listsinceblock(blockhash='', targetconf=1, includeWatchOnly=False):
    data = '{'+rpc.get_request_metadata()+', "method": "listsinceblock", "params": ["' + str(blockhash) + '", ' + str(targetconf) + ', ' + str(includeWatchOnly).lower() + '] }'
    return rpc.rpc_request(data)

# listtransactions with account is deprecated
def listtransactions(account="*", count=10, skip=0, includeWatchOnly=False):
    data = '{'+rpc.get_request_metadata()+', "method": "listtransactions", "params": ["*", ' + str(count) + ', ' + str(skip) + ', ' + str(includeWatchOnly).lower() + '] }'
    return rpc.rpc_request(data)

def listunspent(minconf=1, maxconf=9999999, addresses=[""]):
    addr_list = "[";
    for addr in addresses:
        # it seems Komodo rpc considers ' and " differently.. so instead of just str(addresses), have to do this
        addr_list += "\"" + str(addr) + "\","
    if (len(addresses) > 0):
        addr_list = addr_list[:-1]
    addr_list += "]";
    data = '{'+rpc.get_request_metadata()+', "method": "listunspent", "params": [' + str(minconf) + ', ' + str(maxconf) + ', ' + addr_list + '] }'
    return rpc.rpc_request(data)

# See the listunspent and listlockunspent calls to determine local transaction state and info.
def lockunspent(unlock=False, txid='', vout=0):
    data = '{'+rpc.get_request_metadata()+', "method": "lockunspent", "params": [' + str(
        unlock).lower() + ', [{"txid":"' + str(txid) + '","vout":' + str(vout) + '}]] }'
    return rpc.rpc_request(data)

def resendwallettransactions():
    data = '{'+rpc.get_request_metadata()+', "method": "resendwallettransactions", "params": [] }'
    return rpc.rpc_request(data)

# account MUST be set to the empty string "" to represent the default account
# incomplete: does not considers last two parameters: subtractFeeFromAmt and address
def sendmany(account='', amounts={'': 0}, minconf=1, comment='', subtractFeeFromAmt=[""], address=''):
    amount_list = "{";
    for amt in amounts:
        amount_list += "\"" + amt + "\":" + str(amounts[amt]) + ","
    if (len(amounts) > 0):
        amount_list = amount_list[:-1]
    amount_list += "}"
    '''
    subtractFeeFrom_list = "[";
    for addr in subtractFeeFromAmt:
        subtractFeeFrom_list += "\""+str(addr)+"\","
    subtractFeeFrom_list = subtractFeeFrom_list[:-1]
    subtractFeeFrom_list += "]"
    '''
    data = '{'+rpc.get_request_metadata()+', "method": "sendmany", "params": ["", ' + amount_list + ', ' + str(minconf) + ', "' + str(comment) + '"] }'
    return rpc.rpc_request(data)

def sendtoaddress(address='', amount=0.0, comment='', comment_to='', subtractFeeFromAmt=False):
    data = '{'+rpc.get_request_metadata()+', "method": "sendtoaddress", "params": ["' + str(address) + '", ' + str(
        amount) + ', "' + str(comment) + '", "' + str(comment_to) + '", ' + str(subtractFeeFromAmt).lower() + '] }'
    return rpc.rpc_request(data)

# This method works only once per daemon start. It can't be used to change the pubkey that has already been set.
def setpubkey(pubKey=''):
    data = '{'+rpc.get_request_metadata()+', "method": "setpubkey", "params": ["' + str(pubKey) + '"] }'
    return rpc.rpc_request(data)

def settxfee(amount=0.0):
    data = '{'+rpc.get_request_metadata()+', "method": "settxfee", "params": [' + str(amount) + '] }'
    return rpc.rpc_request(data)

def signmessage(address='', message=''):
    data = '{'+rpc.get_request_metadata()+', "method": "signmessage", "params": ["' + str(address) + '", "' + str(message) + '"] }'
    return rpc.rpc_request(data)

def z_exportkey(z_address=''):
    data = '{'+rpc.get_request_metadata()+', "method": "z_exportkey", "params": ["'+str(z_address)+'"] }'
    return rpc.rpc_request(data)

def z_exportviewingkey(z_address=''):
    data = '{'+rpc.get_request_metadata()+', "method": "z_exportviewingkey", "params": ["'+str(z_address)+'"] }'
    return rpc.rpc_request(data)

def z_exportwallet(filename='z_wallet_export'):
    data = '{'+rpc.get_request_metadata()+', "method": "z_exportwallet", "params": ["'+str(filename)+'"] }'
    return rpc.rpc_request(data)

def z_getbalance(address='', minconf=1):
    data = '{'+rpc.get_request_metadata()+', "method": "z_getbalance", "params": ["'+str(address)+'", '+str(minconf)+'] }'
    return rpc.rpc_request(data)

def z_getnewaddress():
    data = '{'+rpc.get_request_metadata()+', "method": "z_getnewaddress", "params": [] }'
    return rpc.rpc_request(data)

def z_getoperationresult(operationid=['']):
    oppid_list = "[";
    for oppid in operationid:
        oppid_list += "\"" + str(oppid) + "\","
    if (len(operationid) > 0):
        oppid_list = oppid_list[:-1]
    oppid_list += "]";
    data = '{'+rpc.get_request_metadata()+', "method": "z_getoperationresult", "params": ['+oppid_list+'] }'
    return rpc.rpc_request(data)

def z_getoperationstatus(operationid=['']):
    oppid_list = "[";
    for oppid in operationid:
        oppid_list += "\"" + str(oppid) + "\","
    if (len(operationid) > 0):
        oppid_list = oppid_list[:-1]
    oppid_list += "]";
    data = '{'+rpc.get_request_metadata()+', "method": "z_getoperationstatus", "params": ['+oppid_list+'] }'
    return rpc.rpc_request(data)

def z_gettotalbalance(minconf=1, includeWatchOnly=False):
    data = '{'+rpc.get_request_metadata()+', "method": "z_gettotalbalance", "params": ['+str(minconf)+', '+str(includeWatchOnly).lower()+'] }'
    return rpc.rpc_request(data)

def z_importkey(z_privatekey='', rescan='whenkeyisnew', startHeight=0):
    data = '{'+rpc.get_request_metadata()+', "method": "z_importkey", "params": ["'+str(z_privatekey)+'", "'+str(rescan)+'", '+str(startHeight)+'] }'
    return rpc.rpc_request(data)

def z_importviewingkey(viewing_key='', rescan='whenkeyisnew', startHeight=0):
    data = '{'+rpc.get_request_metadata()+', "method": "z_importviewingkey", "params": ["'+str(viewing_key)+'", "'+str(rescan)+'", '+str(startHeight)+'] }'
    return rpc.rpc_request(data)

def z_importwallet(filename=''):
    data = '{'+rpc.get_request_metadata()+', "method": "z_importwallet", "params": ["'+str(filename)+'"] }'
    return rpc.rpc_request(data)

def z_listaddresses(includeWatchOnly=False):
    data = '{'+rpc.get_request_metadata()+', "method": "z_listaddresses", "params": ['+str(includeWatchOnly).lower()+'] }'
    return rpc.rpc_request(data)

def z_listoperationids(status=''):
    data = '{'+rpc.get_request_metadata()+', "method": "z_listoperationids", "params": ["'+str(status)+'"] }'
    return rpc.rpc_request(data)

def z_listreceivedbyaddress(address='', minconf=1):
    data = '{'+rpc.get_request_metadata()+', "method": "z_listreceivedbyaddress", "params": ["'+str(address)+'", '+str(minconf)+'] }'
    return rpc.rpc_request(data)

def z_listunspent(minconf=1, maxconf=9999999, includeWatchOnly=False, addresses=['']):
    addr_list = "[";
    for addr in addresses:
        addr_list += "\"" + str(addr) + "\","
    if (len(addresses) > 0):
        addr_list = addr_list[:-1]
    addr_list += "]";
    data = '{'+rpc.get_request_metadata()+', "method": "z_listunspent", "params": ['+str(minconf)+', '+str(maxconf)+', '+str(includeWatchOnly).lower()+', '+addr_list+'] }'
    return rpc.rpc_request(data)

def z_mergetoaddress(fromaddresses=[''], toaddress='', fee=0.0001, transparent_limit=50, shielded_limit=10, memo=''):
    addr_list = "[";
    for addr in fromaddresses:
        addr_list += "\"" + str(addr) + "\","
    if (len(fromaddresses) > 0):
        addr_list = addr_list[:-1]
    addr_list += "]";
    data = '{'+rpc.get_request_metadata()+', "method": "z_mergetoaddress", "params": ['+addr_list+', "'+str(toaddress)+'"'+(', '+str(fee) if fee != 0.0001 else '')+(', '+str(transparent_limit) if transparent_limit != 50 else '')+(', '+str(shielded_limit) if shielded_limit != 10 else '')+(', "'+str(memo)+'"' if memo != '' else '')+'] }'
    return rpc.rpc_request(data)

def z_sendmany(fromaddress='', amounts={'': 0.0}, memo='', minconf=1, fee=0.0001):
    amount_list = '[';
    for amt in amounts:
        amount_list += '{"address":"' + amt + '", "amount": ' + str(amounts[amt]) + '},'
    if (len(amounts) > 0):
        amount_list = amount_list[:-1]
    amount_list += ']'
    data = '{'+rpc.get_request_metadata()+', "method": "z_sendmany", "params": ["'+str(fromaddress)+'", ' + amount_list +(', "'+str(memo)+'"' if memo != '' else '')+(', '+str(minconf) if minconf != 1 else '')+ (', '+str(fee) if fee != 0.0001 else '')+'] }'
    return rpc.rpc_request(data)

def z_shieldcoinbase(fromaddress='', toaddress='', fee=0.0001, limit=50):
    data = '{'+rpc.get_request_metadata()+', "method": "z_shieldcoinbase", "params": ["'+str(fromaddress)+'", "'+str(toaddress)+(', '+str(fee) if fee != 0.0001 else '')+(', '+str(limit) if limit != 50 else '')+'"] }'
    return rpc.rpc_request(data)

def zcbenchmark(benchmarktype='', samplecount=1):
    data = '{'+rpc.get_request_metadata()+', "method": "zcbenchmark", "params": ["'+str(benchmarktype)+'", '+str(samplecount)+'] }'
    return rpc.rpc_request(data)




