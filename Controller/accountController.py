import ecdsa
# secrets is a cryptographically secure source of random numbers
import secrets
import codecs
from Crypto.Hash import keccak
from Model.account import Account
import locale
locale.setlocale(locale.LC_ALL, '')


class AccountController:
    def __init__(self):
        self.privkeylist = self.getPrivKeyList()
        self.pubkeylist = self.getPubKeyList(self.privkeylist)
        self.walletaddresslist = self.getWalletAddressList(self.pubkeylist)
        self.accountlist = self.constructAccountsList(self.privkeylist, self.pubkeylist, self.walletaddresslist)
        self.writeAccountsToFile(self.accountlist)

    def getPrivKeyList(self):
        self.displaySizeOfAddressUniverse()
        privkeylist = []
        i = 0
        for i in range(self.promptUserForNumberOfPrivateKeys()):
            bits = secrets.randbits(256)
            hex_bits = hex(bits)
            privatekey = hex_bits[2:]
            if len(privatekey) > 63:
                privkeylist.append(privatekey)
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

        with open("./Data/ethereum-accounts.txt", "w", encoding='utf-8') as f:
            f.write('\t\t' + "Generated List of Potential Ethereum Accounts!" + '\n')
            f.write("***********************************************************************************************************************************************" + '\n')
            for i in range(len(accountlist)):
                f.write("Private Key: " + str(accountlist[i].privkey) + '\n')
                f.write("Public Key: " + str(accountlist[i].pubkey) + '\n')
                f.write("Address: " + str(accountlist[i].address) + '\n')
                f.write("Balance: " + str(accountlist[i].balance) + '\n')
                f.write("***********************************************************************************************************************************************" + '\n')

    def displaySizeOfAddressUniverse(self):
        a = 16
        b = 64
        print("Ethereum Addresses are 64 character long strings in hexadecimal format.")
        print("Therefore, there are 16 \N{SUPERSCRIPT SIX}\N{SUPERSCRIPT FOUR} possible permutations: ")
        print("{:,}".format(a ** b))

    def promptUserForNumberOfPrivateKeys(self):
        return int(input("Enter the number of private keys you would like to generate: "))


