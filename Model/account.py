# Account class to hold private key, public key, address, balance


class Account:
    def __init__(self, _privkey, _pubkey, _address, _balance=0):
        self.privkey = _privkey
        self.pubkey = _pubkey
        self.address = _address
        self.balance = _balance

    def getPrivKey(self):
        return self.privkey

    def getPubKey(self):
        return self.pubkey

    def getAddress(self):
        return self.address

    def getBalance(self):
        return self.balance

    def insufficientFunds(self, _amount):
        if self.balance < _amount:
            return True
        else:
            return False

    def sendAmount(self, _recipientaddress, _amount):
        recipientaddress = _recipientaddress
        amount = _amount
        if not self.insufficientFunds(amount):
            tx = Transaction(recipientaddress, self.address, amount)
            return tx
        else:
            print("Insufficient funds to complete transaction")

    def __str__(self):
        print("Private Key: " + str(self.privkey))
        print("Public Key: " + str(self.pubkey))
        print("Addresss: " + str(self.address))
        print("Balance: " + str(self.balance))
        return ''


class Transaction:
    def __init__(self, _recipientaddress, _senderaddress, _amount):
        self.recipientaddress = _recipientaddress
        self.senderaddress = _senderaddress
        self.amount = _amount
