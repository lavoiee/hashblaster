

# secrets is a cryptographically secure source of random numbers
import secrets
import ecdsa
import codecs
from Crypto.Hash import keccak

from accountController import AccountController

accControl = AccountController()

privKeyList = []
pubKeyList = []
walletAddressList = []

i = 0
for i in range(100000):
    bits = secrets.randbits(256)
    hex_bits = hex(bits)
    privatekey = hex_bits[2:]
    if len(privatekey) > 63:
        privKeyList.append(privatekey)

increment = 0
with open("ethpriv-keys.txt", "w", encoding='utf-8') as f:
    f.write('\t\t' + "Generated List of Private Keys!" + '\n')
    for x in privKeyList:
        increment += 1
        f.write(str(increment) + ': ' + x + '\n')

for x in privKeyList:
    private_key_bytes = codecs.decode(x, 'hex')
    # Get ECDSA public key
    key = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1).verifying_key
    key_bytes = key.to_string()
    publickey = codecs.encode(key_bytes, 'hex')
    pubKeyList.append(publickey)

increment = 0
with open("ethpub-keys.txt", "w", encoding='utf-8') as f:
    f.write('\t\t' + "Generated List of Public Keys!" + '\n')
    for x in pubKeyList:
        increment += 1
        f.write(str(increment) + ': ' + str(x) + '\n')


for x in pubKeyList:
    public_key_bytes = codecs.decode(x, 'hex')
    keccak_hash = keccak.new(digest_bits=256)
    keccak_hash.update(public_key_bytes)
    keccak_digest = keccak_hash.hexdigest()
    wallet_length = 40
    wallet = '0x' + keccak_digest[-wallet_length:]
    walletAddressList.append(wallet)

increment = 0

with open("ethAddresses.txt", "w", encoding='utf-8') as f:
    f.write('\t\t' + "Generated List of Wallet Addreses!" + '\n')
    for x in walletAddressList:
        increment += 1
        f.write(str(increment) + ': ' + str(x) + '\n')