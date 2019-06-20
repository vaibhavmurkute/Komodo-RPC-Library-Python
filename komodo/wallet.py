import rpc_util.rpc as rpc

def getwalletinfo():
    '''
    The getwalletinfo method returns an object containing various
    information about the wallet state.
    :return: JSON string:
            "walletversion" (numeric) the wallet version
            "balance" (numeric) the total confirmed balance of the wallet
            "unconfirmed_balance" (numeric) the total unconfirmed
                balance of the wallet
            "immature_balance" (numeric) the total immature balance
                of the wallet
            "txcount" (numeric) the total number of transactions
                in the wallet
            "keypoololdest" (numeric) the timestamp (seconds since GMT
                epoch) of the oldest pre-generated key in the key pool
            "keypoolsize" (numeric) how many new keys are pre-generated
            "unlocked_until" (numeric) the timestamp in seconds since
                epoch (midnight Jan 1 1970 GMT) that the wallet is
                unlocked for transfers, or 0 if the wallet is locked
            "paytxfee" (numeric) the transaction fee configuration,
                given as the relevant COIN per KB
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "getwalletinfo", ' \
                '"params": [] }'
    return rpc.rpc_request(data)

def backupwallet(filename):
    '''
    The backupwallet method safely copies the wallet.dat file
    to the indicated destination.
    This method requires that the coin daemon have the exportdir
    runtime parameter enabled.
    :param "destination" (string, required) the destination filename,
        saved in the directory set by the exportdir runtime parameter
    :return: "path" (JSON string) the full path of the destination file
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "backupwallet", ' \
                '"params": ["' + str(filename) + '"] }'
    return rpc.rpc_request(data)

def dumpprivkey(address):
    '''
    The dumpprivkey method reveals the private key corresponding
    to the indicated address.
    :param "address" (string, required) the address for the private key
    :return: "data" (JSON string) the private key
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "dumpprivkey", ' \
                '"params": ["' + str(address) + '"] }'
    return rpc.rpc_request(data)

def dumpwallet(filename):
    '''
    The dumpwallet method dumps all transparent-address wallet keys
    into a file, using a human-readable format.
    :param: "filename" (string, required) the filename, saved in the
        folder set by the exportdir runtime parameter.
    :return: "path" (JSON string) the full path of the destination file
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "dumpwallet", ' \
                '"params": ["' + str(filename) + '"] }'
    return rpc.rpc_request(data)

def encryptwallet(passphrase=''):
    '''
    The encryptwallet method encrypts the wallet with the
    indicated passphrase.
    :param passphrase (string) the passphrase for wallet encryption;
        the passphrase must be at least 1 character, but should be many
    :return: (JSON String) wallet encrypted; Komodo server stopping,
        restart to run with encrypted wallet. The keypool has been flushed,
        you need to make a new backup.
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "encryptwallet", ' \
                '"params": ['+str(passphrase)+'] }'
    return rpc.rpc_request(data)

def getaccount(address):
    '''
    The getaccount method returns the account associated with
    the given address.
    :param address (string, required) the address
    :return: "accountname" (JSON string) the account address
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "getaccount", ' \
                '"params": ["' + str(address) + '"] }'
    return rpc.rpc_request(data)

def getbalance(account='', minconf=1, includeWatchOnly=False):
    '''
    The getbalance method returns the server's total available balance.
    The account input is deprecated.
    :param account (string, optional) DEPRECATED if provided, it MUST be
        set to the empty string "" or to the string "*"
    :param minconf (numeric, optional, default=1) only include
        transactions confirmed at least this many times
    :param includeWatchOnly:(bool, optional, default=false)	also include
        balance in watchonly addresses
    :return: amount	(JSON string)	the total amount
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "getbalance", ' \
                '"params": ["",1] }'
    return rpc.rpc_request(data)

def getnewaddress(account=''):
    '''
    The getnewaddress method returns a new address for receiving payments
    :param account (string, optional) DEPRECATED: If provided, the account
        MUST be set to the empty string "" to represent the default account
    :return: "address" (JSON string) the new address
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "getnewaddress", ' \
                '"params": [] }'
    return rpc.rpc_request(data)

def getrawchangeaddress():
    '''
    The getrawchangeaddress returns a new address that can be used
    to receive change.
    :return: "address" (JSON string) the address
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "getrawchangeaddress", ' \
                '"params": [] }'
    return rpc.rpc_request(data)

def getreceivedbyaddress(address='', minconf=1):
    '''
    The getreceivedbyaddress method returns the total amount received
    by the given address in transactions with at least minconf confirmations
    :param address (string, required) the address for transactions
    :param minconf (numeric, optional, default=1) only include
        transactions confirmed at least this many times
    :return: amount	(JSON string) the total amount of the relevant coin
        received at this address
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "getreceivedbyaddress", ' \
                '"params": ["' + str(address) + '", ' + str(minconf) + '] }'
    return rpc.rpc_request(data)

def gettransaction(txid, includeWatchOnly=False):
    '''
    The gettransaction method queries detailed information about
    transaction txid. This command applies only to txid's that are in
    the user's local wallet
    :param txid: (string, required)	the transaction id
    :param includeWatchOnly: (bool, optional, default=false) whether to
        include watchonly addresses in the returned balance calculation and
        in the details[] returned values
    :return: JSON string with transaction details
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "gettransaction", ' \
                '"params": ["' + str(txid) + ', ' + \
                    str(includeWatchOnly) + '"] }'
    return rpc.rpc_request(data)

def getunconfirmedbalance():
    '''
    The getunconfirmedbalance method returns the server's total
    unconfirmed balance
    :return: JSON string
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "getunconfirmedbalance", ' \
                '"params": [] }'
    return rpc.rpc_request(data)

def importaddress(address, label='', rescan=True):
    '''
    The importaddress method adds an address or script (in hex) that
    can be watched as if it were in your wallet, although it cannot be
    used to spend. This call can take an increased amount of time to
    complete if rescan is true.
    :param address:(string, required) the address to watch
    :param label:(string, optional, default="")	an optional label
    :param rescan: (boolean, optional, default=true) rescan the
        wallet for transactions
    :return: JSON string
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "importaddress", ' \
                '"params": ["' + str(address) + '", "' + \
                    str(label) + '", ' + str(rescan).lower() + '] }'
    return rpc.rpc_request(data)

def importprivkey(privKey='', label='', rescan=True):
    '''
    The importprivkey method adds a private key to your wallet.
    :param privKey: (string, required) the private key
    :param label: (string, optional, default="") an optional label
    :param rescan: (boolean, optional, default=true) rescan the wallet
        for transactions
    :return: addresses (JSON string) the public address
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "importprivkey", ' \
                '"params": ["'+str(privKey)+'", "'+str(label)+\
                    '",'+str(rescan).lower()+'] }'
    return rpc.rpc_request(data)

def importwallet(path):
    '''
    The importwallet method imports transparent-address keys from
    a wallet-dump file
    :param path:(string, required) the wallet file
    :return:JSON string
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "importwallet", ' \
                '"params": ["' + str(path) + '"] }'
    return rpc.rpc_request(data)

def keypoolrefill(newsize=100):
    '''
    The keypoolrefill method refills the keypool
    :param newsize:(numeric, optional, default=100)	the new keypool size
    :return:JSON string
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "keypoolrefill", ' \
                '"params": [' + str(newsize) + '] }'
    return rpc.rpc_request(data)

def listaddressgroupings():
    '''
    The listaddressgroupings method lists groups of addresses which
    have had their common ownership made public by common use as inputs
    or as the resulting change in past transactions
    :return: JSON string
        "address" (string) the address
        amount (numeric) the amount
        "account" (string, optional) (DEPRECATED) the account
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "listaddressgroupings", ' \
                '"params": [] }'
    return rpc.rpc_request(data)

def listlockunspent():
    '''
    The listlockunspent method returns a list of temporarily
    non-spendable outputs
    :return: JSON string
        "txid" (string)	the transaction id locked
        "vout" (numeric) the vout value
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "listlockunspent", ' \
                '"params": [] }'
    return rpc.rpc_request(data)

def listreceivedbyaddress(minconf=1, includeEmpty=False, includeWatchOnly=False):
    '''
    The listreceivedbyaddress method lists balances by receiving address
    :param minconf:(numeric, optional, default=1) the minimum number of
        confirmations before payments are included
    :param includeEmpty:(numeric, optional, default=false) whether to
        include addresses that haven't received any payments
    :param includeWatchOnly:(bool, optional, default=false)	whether to
        include watchonly addresses (see 'importaddress')
    :return:JSON string:
        "involvesWatchonly"	(bool) only returned if imported addresses were
            involved in transaction
        "address" (string) the receiving address
        "account" (string) DEPRECATED the account of the receiving address;
            the default account is ""
        "amount" (numeric) the total amount received by the address
        "confirmations"	(numeric) a confirmation number that is dPoW aware;
        "rawconfirmations" (numeric) the raw confirmations of the most
            recent transaction included (number of blocks on top of this
            transaction's block)
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "listreceivedbyaddress", ' \
                '"params": [' + str(minconf) + ', ' +\
                    str(includeEmpty).lower() + ', ' +\
                    str(includeWatchOnly).lower() + '] }'
    return rpc.rpc_request(data)


def listsinceblock(blockhash='', targetconf=1, includeWatchOnly=False):
    '''
    The listsinceblock method queries all transactions in blocks since
    block blockhash, or all transactions if blockhash is omitted
    :param blockhash: (string, optional) the block hash from which
        to list transactions
    :param targetconf: (numeric, optional) the confirmations required
        (must be 1 or more)
    :param includeWatchOnly: (bool, optional, default=false) include
        transactions to watchonly addresses
    :return: JSON string with block details
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "listsinceblock", ' \
                '"params": ["' + str(blockhash) + '", ' +\
                    str(targetconf) + ', ' + str(includeWatchOnly).lower() +\
           '] }'
    return rpc.rpc_request(data)

def listtransactions(account="*", count=10, skip=0, includeWatchOnly=False):
    '''
    The listtransactions method returns up to count most recent
    transactions skipping the first from transactions for account.
    :param account: (string, optional)	DEPRECATED the account name;
        should be "*"
    :param count:(numeric, optional, default=10) the number of
        transactions to return
    :param skip: (numeric, optional, default=0)	the number of
        transactions to skip
    :param includeWatchOnly: (bool, optional, default=false) include
        transactions to watchonly addresses
    :return: JSON string with transactin details
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "listtransactions", ' \
                '"params": ["*", ' + str(count) + ', ' + str(skip) +\
                    ', ' + str(includeWatchOnly).lower() + '] }'
    return rpc.rpc_request(data)

def listunspent(minconf=1, maxconf=9999999, addresses=[""]):
    '''
    The listunspent method returns an array of unspent transaction
    outputs, with a range between minconf and maxconf (inclusive)
    confirmations.
    :param minconf:(numeric, optional, default=1) the minimum
        confirmations to filter
    :param maxconf:(numeric, optional, default=9999999)	the maximum
        confirmations to filter
    :param addresses:(string) a series of addresses
    :return: JSON string:
        "txid" (string) the transaction id
        "vout" (numeric) the vout value
        "generated"	(boolean) true if txout is a coinbase transaction
            output
        "address" (string) the address
        "account" (string) DEPRECATED the associated account, or "" for
            the default account
        "scriptPubKey" (string) the script key
        "amount" (numeric) the transaction amount
        "confirmations"	(numeric) a confirmation number that is dPoW aware
        "rawconfirmations" (numeric) the raw confirmations (number of
            blocks on top of this transaction's block)
    '''
    addr_list = "[";
    for addr in addresses:
        # it seems Komodo rpc considers ' and " differently.
        # So instead of just str(addresses), have to change ' to "
        addr_list += "\"" + str(addr) + "\","
    if (len(addresses) > 0):
        addr_list = addr_list[:-1]
    addr_list += "]";
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "listunspent", ' \
                '"params": [' + str(minconf) + ', ' + str(maxconf) +\
                    ', ' + addr_list + '] }'
    return rpc.rpc_request(data)

def lockunspent(unlock=False, txid='', vout=0):
    '''
    The lockunspent method locks (unlock = false) or unlocks
    (unlock = true) specified transaction outputs.
    :param unlock:(boolean, required)	whether to unlock (true)
        or lock (false) the specified transactions
    :param txid:(string) the transaction id
    :param vout:(numeric) the output number
    :return: true/false	(JSON string) whether the command was successful
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "lockunspent", ' \
                '"params": [' + str(unlock).lower() +\
                    ', [{"txid":"' + str(txid) + '","vout":' + str(vout) + \
           '}]] }'
    return rpc.rpc_request(data)

def resendwallettransactions():
    '''
    The resendwallettransactions method immediately re-broadcasts
    unconfirmed wallet transactions to all peers.
    :return: "transaction_id" (JSON string) an array of the rebroadcasted
        transaction id's
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "resendwallettransactions", ' \
                '"params": [] }'
    return rpc.rpc_request(data)

def sendmany(account='', amounts={'': 0}, minconf=1, comment='',
             subtractFeeFromAmt=['']):
    '''
    The sendmany method can send multiple transactions at once.
    Amounts are double-precision floating point numbers
    :param account:(string, required) MUST be set to the
        empty string "" to represent the default account;
        passing any other string will result in an error
    :param amounts:{"string":numeric} dictionary with the address (string)
        and the value (double-precision floating numeric)
    :param minconf:(numeric, optional, default=1) only use the balance
        confirmed at least this many times
    :param comment: (string, optional) a string comment
    :param subtractFeeFromAmt: [string, optional] (string, optional) a
        string list with addresses. The fee will be equally deducted
        from the amount of each selected address; the recipients will
        receive less than you enter in their corresponding amount field.
    :return: "transaction_id" (JSON string) the transaction id for the send;
        only 1 transaction is created regardless of the number of addresses
    '''
    amount_list = "{";
    for addr in amounts:
        amount_list += "\"" + addr + "\":" + str(amounts[addr]) + ","
    if (len(amounts) > 0):
        amount_list = amount_list[:-1]
    amount_list += "}"

    subtractFeeFrom_list = "[";
    for addr in subtractFeeFromAmt:
        subtractFeeFrom_list += "\""+str(addr)+"\","
    if (len(subtractFeeFromAmt) > 0):
        subtractFeeFrom_list = subtractFeeFrom_list[:-1]
    subtractFeeFrom_list += "]"

    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "sendmany", ' \
                '"params": ["", ' + amount_list + ', ' + str(minconf) +\
                    ', "' + str(comment) + '", '+subtractFeeFrom_list+'] }'
    return rpc.rpc_request(data)

def sendtoaddress(address='', amount=0.0, comment='', comment_to='',
                  subtractFeeFromAmt=False):
    '''
    The sendtoaddress method sends an amount to a given address.
    The amount is real and is rounded to the nearest 0.00000001
    :param address: (string, required)	the receiving address
    :param amount: (numeric, required) the amount to send (json requires
        all decimals values less than 1 begin with the characters '0.')
    :param comment: (string, optional)	a comment used to store what the
        transaction is for; this is not part of the transaction,
        just kept in your wallet
    :param comment_to: (string, optional) a comment to store the name
        of the person or organization to which you're sending the
        transaction; this is stored in your local wallet file only
    :param subtractFeeFromAmt: (boolean, optional, default=false)
        when true, the fee will be deducted from the amount being sent
    :return: "transaction_id" (JSON string) the transaction id
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "sendtoaddress", ' \
                '"params": ["' + str(address) + '", ' + str(amount) +\
                    ', "' + str(comment) + '", "' + str(comment_to) +\
                    '", ' + str(subtractFeeFromAmt).lower() + '] }'
    return rpc.rpc_request(data)

def setpubkey(pubKey=''):
    '''
    The setpubkey method sets the indicated pubkey. This method
    can be used in place of the pubkey launch parameter, when necessary.
    :param pubKey:(string) the desired pubkey
    :return: JSON string:
        pubkey (string) the pubkey
        ismine (boolean) indicates whether the address belongs to the user
        R-address (string) the public address associated with the pubkey
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "setpubkey", ' \
                '"params": ["' + str(pubKey) + '"] }'
    return rpc.rpc_request(data)

def settxfee(amount=0.0):
    '''
    The settxfee method sets the transaction fee per kB
    :param amount: (numeric, required) the transaction fee in COIN/kB
        rounded to the nearest 0.00000001
    :return: true/false	(JSON string) returns true if successful
    '''
    data = '{'+rpc.get_request_metadata()+',' \
                ' "method": "settxfee", ' \
                '"params": [' + str(amount) + '] }'
    return rpc.rpc_request(data)

def signmessage(address='', message=''):
    '''
    The signmessage method signs a message via the private key of
    an address.
    :param address: (string, required) the address to use for the
        private key
    :param message:(string, required) the message
    :return: "signature" (JSON string) the signature of the message encoded
        in base 64
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "signmessage", ' \
                '"params": ["' + str(address) + '", "' + str(message) + '"] }'
    return rpc.rpc_request(data)

def walletlock():
    '''
    The walletlock method re-locks a wallet that has a passphrase
    enabled via encryptwallet.
    :return: JSON string
    '''
    data = '{' + rpc.get_request_metadata() + ', ' \
                '"method": "walletlock", ' \
                '"params": [] }'
    return rpc.rpc_request(data)

def walletpassphrase(passphrase='', timeout=0):
    '''
    The walletpassphrase method unlocks the wallet using the passphrase
    that was set by the encryptwallet method.
    :param passphrase: (string)	the passphrase that was set by the
        encryptwallet method
    :param timeout:(number in seconds, optional) the amount of time for
        which the wallet should remember the passphrase
    :return: JSON string
    '''
    data = '{' + rpc.get_request_metadata() + ', ' \
                '"method": "walletpassphrase", ' \
                '"params": ["'+str(passphrase)+'", '+str(timeout)+'] }'
    return rpc.rpc_request(data)

def walletpassphrasechange(oldpassphrase='', newpassphrase=''):
    '''
    The walletpassphrasechange method changes "oldpassphrase" to
        "newpassphrase".
    :param oldpassphrase:(string) the old passphrase
    :param newpassphrase:(string) the new passphrase
    :return: JSON string
    '''
    data = '{' + rpc.get_request_metadata() + ', ' \
                '"method": "walletpassphrasechange", ' \
                '"params": ["'+str(oldpassphrase)+'", "'+str(newpassphrase)+\
           '"] }'
    return rpc.rpc_request(data)

def z_exportkey(z_address=''):
    '''
    The z_exportkey method reveals the private z_key
    corresponding to z_address
    :param z_address:(string, required)	the z_address
        for the private key
    :return: "key" (JSON string) the private key
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "z_exportkey", ' \
                '"params": ["'+str(z_address)+'"] }'
    return rpc.rpc_request(data)

def z_exportviewingkey(z_address=''):
    '''
    The z_exportviewingkey method reveals the viewing key
    corresponding to z_address
    :param z_address: (string, required) the z_address for the viewing key
    :return: "vkey"	(JSON string) the viewing key
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "z_exportviewingkey", ' \
                '"params": ["'+str(z_address)+'"] }'
    return rpc.rpc_request(data)

def z_exportwallet(filename='z_wallet_export'):
    '''
    The z_exportwallet method exports all wallet keys, including
    both t address and z address types, in a human-readable format.
    Overwriting an existing file is not permitted
    :param filename:(string, required)	the filename, saved to the
        directory indicated by the exportdir parameter at daemon runtime
    :return: "path"	(JSON string) the full path of the destination file
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "z_exportwallet", ' \
                '"params": ["'+str(filename)+'"] }'
    return rpc.rpc_request(data)

def z_getbalance(address='', minconf=1):
    '''
    The z_getbalance method returns the balance of a t address or
    z address belonging to the node’s wallet.
    :param address:(string)	the selected z or t address
    :param minconf: (numeric, optional, default=1)	only include
        transactions confirmed at least this many times
    :return: amount	(JSON numeric)	the total amount received at
        this address (in the relevant COIN value)
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "z_getbalance", ' \
                '"params": ["'+str(address)+'", '+str(minconf)+'] }'
    return rpc.rpc_request(data)

def z_getnewaddress():
    '''
    The z_getnewaddress method returns a new z_address for receiving
    payments
    :return: "z_address" (JSON string) the new z_address
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "z_getnewaddress", ' \
                '"params": [] }'
    return rpc.rpc_request(data)

def z_getoperationresult(operationid=['']):
    '''
    The z_getoperationresult method retrieves the result and status
    of an operation which has finished, and then removes the operation
    from memory
    :param operationid: [string, optional]	a list of operation ids to
        query; if not provided, the method examines all operations
        known to the node
    :return: JSON String
        "id" (string) the operation id
        "status" (string) the result of the operation; can be success
        "creation_time" (numeric) the creation time, in seconds since
            epoch (Jan 1 1970 GMT)
        "result": { ... } (array of json objects)
        "txid":	(string) the transaction id
        "execution_secs" (numeric) the length of time to calculate the
            transaction
        "method" (string) the name of the method used in the operation
        "params": { ... } (json)
        "fromaddress" (string) the address from which funds are drawn
        "amounts": [ ... ]	(array of json objects)
        "address" (string) the receiving address
        "amount" (numeric) the amount to receive
        "minconf" (numeric)	the minimum number of confirmations required
        "fee" (numeric) the transaction fee
    '''
    oppid_list = "[";
    for oppid in operationid:
        oppid_list += "\"" + str(oppid) + "\","
    if (len(operationid) > 0):
        oppid_list = oppid_list[:-1]
    oppid_list += "]";
    data = '{'+rpc.get_request_metadata()+', "method": "z_getoperationresult", "params": ['+oppid_list+'] }'
    return rpc.rpc_request(data)

def z_getoperationstatus(operationid=['']):
    '''
    The z_getoperationstatus message queries the operation status
    and any associated result or error data of any operationid stored
    in local memory.
    :param operationid: [string, optional]	a list of operation-ids
        we are interested in; if an array is not provided, the method
        examines all operations known to the node
    :return: JSON string with operation details
    '''
    oppid_list = "[";
    for oppid in operationid:
        oppid_list += "\"" + str(oppid) + "\","
    if (len(operationid) > 0):
        oppid_list = oppid_list[:-1]
    oppid_list += "]";
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "z_getoperationstatus", ' \
                '"params": ['+oppid_list+'] }'
    return rpc.rpc_request(data)

def z_gettotalbalance(minconf=1, includeWatchOnly=False):
    '''
    The z_gettotalbalance method returns the total value of funds,
    including both transparent and private, stored in the node’s wallet
    :param minconf: (numeric, optional, default=1) only include private
        and transparent transactions confirmed at least this many times
    :param includeWatchOnly: (bool, optional, default=false) also include
        balance in watchonly addresses
    :return: JSON string:
        "transparent" (numeric) the total balance of transparent funds
        "interest" (numeric) the total balance of unclaimed interest
            earned
        "private" (numeric)	the total balance of private funds
        "total"	(numeric) the total balance of both transparent and
            private funds
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "z_gettotalbalance", ' \
                '"params": ['+str(minconf)+', '+str(includeWatchOnly).lower()+\
           '] }'
    return rpc.rpc_request(data)

def z_importkey(z_privatekey='', rescan='whenkeyisnew', startHeight=0):
    '''
    The z_importkey method imports z_privatekey to your wallet.
    This call can take minutes to complete if rescan is true
    :param z_privatekey: (string, required)	the z_privatekey
    :param rescan: (string, optional, default="whenkeyisnew") rescan
        the wallet for transactions; can be yes
    :param startHeight: (numeric, optional, default=0) the block
        height at which to begin the rescan
    :return: JSON string
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "z_importkey", ' \
                '"params": ["'+str(z_privatekey)+'", "'+\
                    str(rescan)+'", '+str(startHeight)+'] }'
    return rpc.rpc_request(data)

def z_importviewingkey(viewing_key='', rescan='whenkeyisnew', startHeight=0):
    '''
    The z_importviewingkey adds a viewing key to your wallet.
    This method allows you to view the balance in a z address that
    otherwise does not belong to your wallet.
    :param viewing_key: (string, required)	the viewing key
    :param rescan: (string, optional, default="whenkeyisnew") whether
        to rescan the wallet for transactions; can be "yes"
    :param startHeight: (numeric, optional, default=0) block height
        to start rescan
    :return: JSON string
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "z_importviewingkey", ' \
                '"params": ["'+str(viewing_key)+'", "'+\
                    str(rescan)+'", '+str(startHeight)+'] }'
    return rpc.rpc_request(data)

def z_importwallet(filename=''):
    '''
    The z_importwallet method imports t address and z address keys
    from a wallet export file
    :param filename: (string, required) the wallet file
    :return: JSON String
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "z_importwallet", ' \
                '"params": ["'+str(filename)+'"] }'
    return rpc.rpc_request(data)

def z_listaddresses(includeWatchOnly=False):
    '''
    The z_listaddresses method returns the list of z addresses
    belonging to the wallet.
    :param includeWatchOnly: (bool, optional, default=false) also
        include watchonly addresses
    :return: "z_address" ( JSON string) a z address belonging
        to the wallet
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "z_listaddresses", ' \
                '"params": ['+str(includeWatchOnly).lower()+'] }'
    return rpc.rpc_request(data)

def z_listoperationids(status=''):
    '''
    The z_listoperationids method returns the list of operation
    ids currently known to the wallet.
    :param status: (string, optional) filter result by the
        operation's state e.g. "success"
    :return: "operationid"	(JSON string) an operation id belonging
        to the wallet
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "z_listoperationids", ' \
                '"params": ["'+str(status)+'"] }'
    return rpc.rpc_request(data)

def z_listreceivedbyaddress(address='', minconf=1):
    '''
    The z_listreceivedbyaddress method returns a list of amounts
    received by a z address belonging to the node’s wallet.
    :param address: (string)	the private address.
    :param minconf: (numeric, optional, default=1)	only include
        transactions confirmed at least this many times
    :return: JSON string:
        txid (string) the transaction id
        amount (numeric) the amount of value in the note
        memo (string ) hexadecimal string representation of memo field
        "confirmations"	(numeric) a confirmation number that is
            dPoW aware;
        "rawconfirmations" (numeric) the raw confirmations
            (number of blocks on top of this transaction's block)
        jsindex	(sprout) (numeric, received only by sprout addresses)
            the joinsplit index
        jsoutindex (numeric, received only by sprout addresses)
            the output index of the joinsplit
        outindex (numeric, sapling)	the output index
        change (boolean) true if the address that received the note is also
            one of the sending addresses
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "z_listreceivedbyaddress", ' \
                '"params": ["'+str(address)+'", '+str(minconf)+'] }'
    return rpc.rpc_request(data)

def z_listunspent(minconf=1, maxconf=9999999, includeWatchOnly=False,
                  addresses=['']):
    '''
    The z_listunspent method returns an array of unspent shielded notes
    :param minconf: (numeric, optional, default=1)	the minimum
        confirmations to filter
    :param maxconf: (numeric, optional, default=9999999) the maximum
        confirmations to filter
    :param includeWatchOnly: (bool, optional, default=false) whether
        to also include watchonly addresses
    :param addresses: [string] a list of z addresses (both Sprout and
        Sapling) to act as a filter; duplicate addresses are not allowed
    :return: JSON string
    '''
    addr_list = "[";
    for addr in addresses:
        addr_list += "\"" + str(addr) + "\","
    if (len(addresses) > 0):
        addr_list = addr_list[:-1]
    addr_list += "]";
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "z_listunspent", ' \
                '"params": ['+str(minconf)+', '+str(maxconf)+\
                    ', '+str(includeWatchOnly).lower()+', '+addr_list+'] }'
    return rpc.rpc_request(data)

def z_mergetoaddress(fromaddresses=[''], toaddress='', fee=0.0001,
                     transparent_limit=50, shielded_limit=10, memo=''):
    '''
    The z_mergetoaddress method merges multiple utxos and notes into
    a single utxo or note.
    :param fromaddresses: [string, required] a list of z or t addresses
    :param toaddress: (string, required)	the t address or z address
        to receive the combined utxo
    :param fee: (numeric, optional, default=0.0001)	the fee amount to
        attach to this transaction
    :param transparent_limit: (numeric, optional, default=50) limit on
        the maximum number of transparent utxos to merge; you may set
        this value to 0 to use the node option mempooltxinputlimit
    :param shielded_limit: (numeric, optional, default=10)	limit on
        the maximum number of hidden notes to merge; you may set this
        value to 0 to merge as many as will fit in the transaction
    :param memo: (string, optional)	encoded as hex; when toaddress is
        a z address, this value will be stored in the memo field of the
        new note
    :return: JSON string:
        "remainingUTXOs" (numeric) the number of utxos still
            available for merging
        "remainingTransparentValue" (numeric) the value of utxos still
            available for merging
        "remainingNotes" (numeric) the number of notes still available
            for merging
        "remainingShieldedValue" (numeric) the value of notes still
            available for merging
        "mergingUTXOs" (numeric) the number of utxos being merged
        "mergingTransparentValue" (numeric)	the value of utxos
            being merged
        "mergingNotes" (numeric) the number of notes being merged
        "mergingShieldedValue" (numeric) the value of notes being merged
        "opid" (string) an operationid to pass to z_getoperationstatus
            to get the result of the operation
    '''
    addr_list = "[";
    for addr in fromaddresses:
        addr_list += "\"" + str(addr) + "\","
    if (len(fromaddresses) > 0):
        addr_list = addr_list[:-1]
    addr_list += "]";
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "z_mergetoaddress", ' \
                '"params": ['+addr_list+', "'+str(toaddress)+\
                    '"'+(', '+str(fee) if fee != 0.0001 else '')+\
                    (', '+str(transparent_limit) if transparent_limit != 50 else '')+\
                    (', '+str(shielded_limit) if shielded_limit != 10 else '')+\
                    (', "'+str(memo)+'"' if memo != '' else '')+\
           '] }'
    return rpc.rpc_request(data)

def z_sendmany(fromaddress='', amounts={'': 0.0}, memo='', minconf=1,
               fee=0.0001):
    '''
    The z_sendmany method sends one or more transactions at once, and
    allows for sending transactions of types t --> t, t --> z, z --> z, z --> t.
    :param fromaddress: (string, required) the sending t address or
        z address
    :param amounts: {string : numeric}  a dictionary of z or t address
        as key and numeric amout value to be sent
    :param memo: (string, optional)	if the address is a z address, this
        property accepts raw data represented in hexadecimal string format
    :param minconf: (numeric, optional, default=1)	only use funds
        confirmed at least this many times
    :param fee: (numeric, optional, default=0.0001)	the fee amount to
        attach to this transaction
    :return: "operationid"	(string) an operationid to pass to
        z_getoperationstatus to get the result of the operation
    '''
    amount_list = '[';
    for addr in amounts:
        amount_list += '{"address":"' + addr + '", "amount": ' +\
                        str(amounts[addr]) + '},'
    if (len(amounts) > 0):
        amount_list = amount_list[:-1]
    amount_list += ']'
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "z_sendmany", ' \
                '"params": ["'+str(fromaddress)+'", ' +\
                    amount_list +(', "'+str(memo)+'"' if memo != '' else '')+\
                    (', '+str(minconf) if minconf != 1 else '')+\
                    (', '+str(fee) if fee != 0.0001 else '')+\
           '] }'
    return rpc.rpc_request(data)

def z_shieldcoinbase(fromaddress='', toaddress='', fee=0.0001, limit=50):
    '''
    The z_shieldcoinbase method shields transparent coinbase funds by
    sending the funds to a shielded z address.
    :param fromaddress: (string, required)	the address is a t address
        or "*" for all t address belonging to the wallet
    :param toaddress: (string, required)	the address is a z address
    :param fee: (numeric, optional, default=0.0001)	the fee amount to
        attach to this transaction
    :param limit: (numeric, optional, default=50) limit on the maximum
        number of utxos to shield; set to 0 to use node option
        mempooltxinputlimit
    :return: JSON string:
        "remainingUTXOs" (numeric) the number of coinbase utxos still
            available for shielding
        "remainingValue" (numeric) the value of coinbase utxos still
            available for shielding
        "shieldingUTXOs" (numeric) the number of coinbase utxos
            being shielded
        "shieldingValue" (numeric) the value of coinbase utxos
            being shielded
        "opid" (string) an operationid to pass to z_getoperationstatus
            to get the result of the operation
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "z_shieldcoinbase", ' \
                '"params": ["'+str(fromaddress)+'", "'+\
                    str(toaddress)+(', '+str(fee) if fee != 0.0001 else '')+\
                    (', '+str(limit) if limit != 50 else '')+\
           '"] }'
    return rpc.rpc_request(data)

def zcbenchmark(benchmarktype='', samplecount=1):
    '''
    The zcbenchmark method runs a benchmark of the selected
    benchmarktype. This benchmark is calculated samplecount times.
    :param benchmarktype: (string, required) the type of the benchmark
    :param samplecount: (numeric) the number of samples to take
    :return: "runningtime" (numeric) the time it took to run the
        selected benchmarktype
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "zcbenchmark", ' \
                '"params": ["'+str(benchmarktype)+'", '+str(samplecount)+'] }'
    return rpc.rpc_request(data)






