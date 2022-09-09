#from Modules import merkle_tree
from time import time
import hashlib
import json
from typing import Any, Callable, Iterable

class Blockchain:
    def __init__(self) -> None:
        self.current_transactions = []
        self.chain = []
        self.nodes = set()

        self.new_block(previous_hash=1, proof=100)

    def new_block(self, previous_hash, proof):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'prev_hash': previous_hash or self.hash(self.chain[-1]),
            'merkle_root': self.merkle_root(self.current_transactions),
            'transactions': self.current_transactions,
            'proof': proof #- добавить, когда появятся датчики
        }

        self.chain.append(block)
        self.current_transactions = []

        return block

    def is_valid_chain(self, chain):
        last_block = chain[0]
        current_index = 1
        while current_index < len(chain):
            block = chain[current_index]
            last_block_hash = self.hash(last_block)
            if block['prev_hash'] != last_block_hash:
                return False

            last_block = block
            current_index += 1

        return True

    def new_transaction(self, owner, field_operation_inf: str):
        self.current_transactions.append({
            'owner': owner,
            'field_operation_inf': field_operation_inf
        })

        return self.current_transactions #Возможно, никакого значения возвращать не надо (ИСПРАВИТЬ ПОТОМ!!!)

    @staticmethod
    def hash(block):
        str_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(str_block).hexdigest()

    @staticmethod
    def get_hash(data: Any):
        if isinstance(data, Iterable):
            data = ''.join(data)
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

    @staticmethod
    def merkle_root(transactions):
        merkle_hashes = [hashlib.sha256(transaction.encode('utf-8')).hexdigest() for transaction in transactions]
        while len(merkle_hashes) != 1:
            if (len(transactions) % 2 != 0): #убираем нечётное количество транзакций
                transactions.append(transactions[-1])
            merkle_hashes = [Blockchain.get_hash(merkle_hashes[i:i+2]) for i in range(0, len(merkle_hashes), 2)]
        return merkle_hashes[0]



    @property
    def last_block(self):
        return self.chain[-1]    
        

    def proof_of_work(self, last_block): # return proof (реализовать с появлением датчиков)
        pass
