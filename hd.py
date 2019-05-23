from pywallet import *


def create_address():
    seed = wallet.generate_mnemonic()
    address = wallet.create_wallet(network='btctest')
    print (address)

def address_from_seed(seed):
    address = wallet.create_wallet(network='btctest', seed=seed, children=2)
    print (address)



# create_address()


# address_from_seed("save easy pioneer vanish skill pelican cake document tail soap mail scan")

WALLET_PUBKEY = 'tpubD6NzVbkrYhZ4Xh5EppPTVeJsW9DWVPDH1eHny2ZGDpnaLddVcZoDogE4c8n3V7U8bpJDs4VRScqYgF5uzkVCX1SpW5gajiDHN49hAWfUNJQ'

# user_addr = wallet.create_address(network="btctest", xpub=WALLET_PUBKEY, child=10)
# print("User Address\n", user_addr)


path = "m/44'/1'/0'/0/10"

user_addr = wallet.create_address(network="btctest", xpub=WALLET_PUBKEY, path =path,child=10)
print("User Address\n", user_addr)

