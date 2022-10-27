from sys import exit
from bitcoin.core.script import *

from utils import *
from config import my_private_key, my_public_key, my_address, faucet_address
from ex1 import send_from_P2PKH_transaction
from bitcoin.wallet import CBitcoinSecret

cust1_private_key = CBitcoinSecret(
    'cNm1M3Z526MvZQSaXdyEoeUku3eFhSzUkYKRQCdvZAoCfFJeSYGv')
cust1_public_key = cust1_private_key.pub
cust2_private_key = CBitcoinSecret(
    'cPKdoZ6BfG3rY7FUf9RYrLPnWJk9hybAVRjU4YDhqwEDbxqFDWNE')
cust2_public_key = cust2_private_key.pub
cust3_private_key = CBitcoinSecret(
    'cPLoDraCR52FTqqBQpCLAbzbYxhKi9RN59RqAf3NEYtuJyt6ksvQ')
cust3_public_key = cust3_private_key.pub


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2

# You can assume the role of the bank for the purposes of this problem
# and use my_public_key and my_private_key in lieu of bank_public_key and
# bank_private_key.

ex2a_txout_scriptPubKey = [CBitcoinSecret('cQdaUpxdPJodjP6z5C3iJjx35bxqv4LqexAbyv1DYtfPK48f6VeV').pub, # 我即银行公钥
                           OP_CHECKSIGVERIFY, 
                           OP_1,
                           cust1_private_key.pub,
                           cust2_private_key.pub,
                           cust3_private_key.pub,       #三个客户的公钥
                           OP_3,
                           OP_CHECKMULTISIG
                          ]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0006
    txid_to_spend = (
        'e4b9408d2c84da043882888759fc26d10279566c652929a21bb42fcfc9018fe2')
    utxo_index = 1
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        ex2a_txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)
