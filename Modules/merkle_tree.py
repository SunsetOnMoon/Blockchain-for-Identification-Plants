#from gettext import _TranslationsReader
import hashlib

def merkle_root(transactions):
    merkle_hashes = [hashlib.sha256(transaction.encode('utf-8')).hexdigest() for transaction in transactions]
    while len(merkle_hashes) != 1:
        if (len(transactions) % 2 != 0): #убираем нечётное количество транзакций
            transactions.append(transactions[-1])
        merkle_hashes = [hashlib.sha256((merkle_hashes[i] + merkle_hashes[i + 1]).encode('utf-8')).hexdigest() for i in range(0, len(merkle_hashes), 2)]
        merkle_hashes = merkle_hashes[::2]
    return merkle_hashes[0]