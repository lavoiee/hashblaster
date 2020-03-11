# Account class to hold private key, public key, and address on the blockchain


class Account():
    def __init__(self, _privkey, _pubkey, _address, _balance=0):
        self.privkey = _privkey
        self.pubkey = _pubkey
        self.address = _address
        self.balance = _balance

    def getPrivKey(self):
        return self.privkey

    def getPubKey(self):
        return self.getPubKey

    def getAddress(self):
        return self.address

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

class Transaction():
    def __init__(self, _recipientaddress, _senderaddress, _amount):
        self.recipientaddress = _recipientaddress
        self.senderaddress = _senderaddress
        self.amount = _amount