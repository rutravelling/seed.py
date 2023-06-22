from bitcoinlib.wallets import HDWallet

def get_private_key(mnemonic):
    # Создаем кошелек из сид-фразы (mnemonic)
    wallet = HDWallet.from_seed(mnemonic, network='bitcoin')

    # Получаем первый приватный ключ
    private_key = wallet.get_key().wif

    return private_key

mnemonic = 'your 12-word seed phrase goes here'
print(get_private_key(mnemonic))
