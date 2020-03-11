import account
import ecdsa
# secrets is a cryptographically secure source of random numbers
import secrets
import codecs
from Crypto.Hash import keccak


class AccountController():
    def __init__(self):
        self.privkeylist = []
        self.pubkeylist = []
        self.walletaddresslist = []
        self.accountlist = []

    def getPrivKeyList(self, _privkeylist):
        self.privkeylist = _privkeylist
        i = 0
        for i in range(100000):
            bits = secrets.randbits(256)
            hex_bits = hex(bits)
            privatekey = hex_bits[2:]
            if len(privatekey) > 63:
                self.privkeylist.append(privatekey)
            increment = 0
            with open("ethpriv-keys.txt", "w", encoding='utf-8') as f:
                f.write('\t\t' + "Generated List of Private Keys!" + '\n')
                for x in self.privkeylist:
                    increment += 1
                    f.write(str(increment) + ': ' + x + '\n')
        return self.privkeylist

    def getPubKeyList(self, _privkeylist, _pubkeylist):
        self.privkeylist = _privkeylist
        self.pubkeylist = _pubkeylist
        for x in self.privkeylist:
            private_key_bytes = codecs.decode(x, 'hex')
            # Get ECDSA public key
            key = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1).verifying_key
            key_bytes = key.to_string()
            publickey = codecs.encode(key_bytes, 'hex')
            self.pubkeylist.append(publickey)
        increment = 0
        with open("ethpub-keys.txt", "w", encoding='utf-8') as f:
            f.write('\t\t' + "Generated List of Public Keys!" + '\n')
            for x in self.pubkeylist:
                increment += 1
                f.write(str(increment) + ': ' + str(x) + '\n')
        return self.pubkeylist

    def getWalletAddressList(self, _pubkeylist):
        self.pubkeylist = _pubkeylist
        for x in self.pubkeylist:
            public_key_bytes = codecs.decode(x, 'hex')
            keccak_hash = keccak.new(digest_bits=256)
            keccak_hash.update(public_key_bytes)
            keccak_digest = keccak_hash.hexdigest()
            wallet_length = 40
            wallet = '0x' + keccak_digest[-wallet_length:]
            self.walletaddresslist.append(wallet)
        increment = 0
        with open("ethAddresses.txt", "w", encoding='utf-8') as f:
            f.write('\t\t' + "Generated List of Wallet Addresses!" + '\n')
            for x in self.walletaddresslist:
                increment += 1
                f.write(str(increment) + ': ' + str(x) + '\n')
        return self.walletaddresslist

