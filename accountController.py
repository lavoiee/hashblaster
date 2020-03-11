import account
import ecdsa
# secrets is a cryptographically secure source of random numbers
import secrets
import codecs
from Crypto.Hash import keccak
from account import Account

numberofaccounts = 10000


class AccountController:

    def __init__(self):
        self.privkeylist = self.getPrivKeyList()
        self.pubkeylist = self.getPubKeyList(self.privkeylist)
        self.walletaddresslist = self.getWalletAddressList(self.pubkeylist)
        self.accountlist = self.constructAccountsList(self.privkeylist, self.pubkeylist, self.walletaddresslist)
        self.writeAccountsToFile(self.accountlist)

    def getPrivKeyList(self):
        privkeylist = []
        i = 0
        for i in range(numberofaccounts):
            bits = secrets.randbits(256)
            hex_bits = hex(bits)
            privatekey = hex_bits[2:]
            if len(privatekey) > 63:
                privkeylist.append(privatekey)
            """
            increment = 0
            with open("ethpriv-keys.txt", "w", encoding='utf-8') as f:
                f.write('\t\t' + "Generated List of Private Keys!" + '\n')
                for x in privkeylist:
                    increment += 1
                    f.write(str(increment) + ': ' + x + '\n')
            """
        return privkeylist

    def getPubKeyList(self, _privkeylist):
        privkeylist = _privkeylist
        pubkeylist = []
        for x in privkeylist:
            private_key_bytes = codecs.decode(x, 'hex')
            # Get ECDSA public key
            key = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1).verifying_key
            key_bytes = key.to_string()
            publickey = codecs.encode(key_bytes, 'hex')
            pubkeylist.append(publickey)

        """
        increment = 0
        with open("ethpub-keys.txt", "w", encoding='utf-8') as f:
            f.write('\t\t' + "Generated List of Public Keys!" + '\n')
            for x in pubkeylist:
                increment += 1
                f.write(str(increment) + ': ' + str(x) + '\n')
        """
        return pubkeylist

    def getWalletAddressList(self, _pubkeylist):
        pubkeylist = _pubkeylist
        walletaddresslist = []
        for x in pubkeylist:
            public_key_bytes = codecs.decode(x, 'hex')
            keccak_hash = keccak.new(digest_bits=256)
            keccak_hash.update(public_key_bytes)
            keccak_digest = keccak_hash.hexdigest()
            wallet_length = 40
            wallet = '0x' + keccak_digest[-wallet_length:]
            walletaddresslist.append(wallet)
        """
        increment = 0
        with open("ethAddresses.txt", "w", encoding='utf-8') as f:
            f.write('\t\t' + "Generated List of Wallet Addresses!" + '\n')
            for x in walletaddresslist:
                increment += 1
                f.write(str(increment) + ': ' + str(x) + '\n')
        """
        return walletaddresslist

    def constructAccountsList(self, _privkeylist, _pubkeylist, _walletaddresslist):
        accountlist = []
        privkeylist = _privkeylist
        pubkeylist = _pubkeylist
        walletaddresslist = _walletaddresslist
        for x in range(len(privkeylist)):
            accountlist.append(Account(privkeylist[x], pubkeylist[x], walletaddresslist[x], 0))
        return accountlist

    def writeAccountsToFile(self, _accountlist):
        accountlist = _accountlist

        with open("ethereum-accounts.txt", "w", encoding='utf-8') as f:
            f.write('\t\t' + "Generated List of Potential Ethereum Accounts!" + '\n')
            f.write("***********************************************************************************************************************************************" + '\n')
            for i in range(len(accountlist)):
                f.write("Private Key: " + str(accountlist[i].privkey) + '\n')
                f.write("Public Key: " + str(accountlist[i].pubkey) + '\n')
                f.write("Address: " + str(accountlist[i].address) + '\n')
                f.write("Balance: " + str(accountlist[i].balance) + '\n')
                f.write("***********************************************************************************************************************************************" + '\n')






