# Account class to hold private key, public key, and address on the blockchain

class Account():
    def __init__(self, _privkey, _pubkey, _address):
        self.privkey = _privkey
        self.pubkey = _pubkey
        self.address = _address

    def __str__(self):
