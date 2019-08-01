import rpc_util.rpc as rpc

def migrate_createburntransaction(destchain_name='', destchain_addr='',
                                  amount=0.0, tokenid=''):
    data = '{' + rpc.get_request_metadata() + ', ' \
                    '"method": "migrate_createburntransaction", ' \
                    '"params": ["'+str(destchain_name)+'",' \
                                    '"'+str(destchain_addr)+'",' \
                                    '"'+str(amount)+'"] }'
    return data


def migrate_converttoexport(burnttx='', destchain=''):
    data = '{' + rpc.get_request_metadata() + ', ' \
                    '"method": "migrate_converttoexport", ' \
                    '"params": ["'+str(burnttx)+'",' \
                                    '"'+str(destchain)+'"] }'
    return data


def migrate_createimporttransaction(burnttx='', payouts='',
                                    notarytxid_n=''):
    data = '{' + rpc.get_request_metadata() + ', ' \
                '"method": "migrate_createimporttransaction", ' \
                '"params": ["'+str(burnttx)+'",' \
                            '"'+str(payouts)+'"'+\
                    ('"'+str(notarytxid_n)+"'" if notarytxid_n != '' else
                     '')+'] }'
    return data


def migrate_completeimporttransaction(importtx='', offset=''):
    data = '{' + rpc.get_request_metadata() + ', ' \
                '"method": "migrate_completeimporttransaction", ' \
                '"params": ["'+str(importtx)+'",' \
                    ('"'+str(offset)+"'" if offset != '' else
                     '')+'] }'
    return data


def migrate_checkburntransactionsource(burntxid=''):
    data = '{' + rpc.get_request_metadata() + ', ' \
                '"method": "migrate_checkburntransactionsource", ' \
                '"params": ["'+str(burntxid)+'"] }'
    return data


def migrate_createnotaryapprovaltransaction (burntxid='', txoutproof=''):
    data = '{' + rpc.get_request_metadata() + ', ' \
                '"method": "migrate_createnotaryapprovaltransaction ", ' \
                '"params": ["'+str(burntxid)+'",' \
                    ('"'+str(txoutproof)+"'")+'] }'
    return data


def selfimport(destaddress='', amount=0.0):
    data = '{' + rpc.get_request_metadata() + ', ' \
                 '"method": "selfimport ", ' \
                    '"params": ["' + str(destaddress) + '",' \
                        ('"' + str(amount) + "'") + '] }'
    return data


def calc_MoM(height=0, MoMdepth=0.0):
    data = '{' + rpc.get_request_metadata() + ', ' \
                 '"method": "calc_MoM ", ' \
                    '"params": ["' + str(height) + '",' \
                        ('"' + str(MoMdepth) + "'") + '] }'
    return data


def MoMoMdata(symbol='', kmdheight=0, ccid=0):
    data = '{' + rpc.get_request_metadata() + ', ' \
                '"method": "MoMoMdata", ' \
                '"params": ["'+str(symbol)+'",' \
                            '"'+str(kmdheight)+'"'+\
                            ('"'+str(ccid)+"'")+'] }'
    return data


def assetchainproof(txid=''):
    data = '{' + rpc.get_request_metadata() + ', ' \
                '"method": "assetchainproof", ' \
                '"params": ["'+str(txid)+'"] }'
    return data


def getNotarisationsForBlock(height=0):
    data = '{' + rpc.get_request_metadata() + ', ' \
                '"method": "getNotarisationsForBlock", ' \
                '"params": ["'+str(height)+'"] }'
    return data


def scanNotarisationsDB(blockheight=0, symbol='',
                                    blockslimit=''):
    data = '{' + rpc.get_request_metadata() + ', ' \
                '"method": "scanNotarisationsDB", ' \
                '"params": ["'+str(blockheight)+'",' \
                            '"'+str(symbol)+'"'+\
                    ('"'+str(blockslimit)+"'" if blockslimit != '' else
                     '')+'] }'
    return data


def getimports(blockhash='', height=0):
    data = '{' + rpc.get_request_metadata() + ', ' \
                '"method": "getimports", ' \
                '"params": ["'+('"'+str(blockhash)+"'" if blockhash != ''
                                    else height)+'"] }'
    return data


def getwalletburntransactions(count=10):
    data = '{' + rpc.get_request_metadata() + ', ' \
                '"method": "getwalletburntransactions", ' \
                '"params": ["'+str(count)+'"] }'
    return data