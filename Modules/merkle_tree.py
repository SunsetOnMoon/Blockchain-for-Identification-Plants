from gettext import _TranslationsReader
import hashlib

def merkle_root(transactions):
    if len(transactions % 2 != 0): #убираем нечётное количество транзакций
        transactions.append(transactions[-1])
    merkle_hashes = [hashlib.sha256(transaction) for transaction in transactions]
    while len(merkle_hashes) != 1:
        merkle_hashes = [hashlib.sha256(merkle_hashes[i] + [i + 1]) for i in range(0, len(merkle_hashes), 2)]
        merkle_hashes = merkle_hashes[::2]

    