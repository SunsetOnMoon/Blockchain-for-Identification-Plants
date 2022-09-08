from time import time

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
            'transactions': self.current_transactions
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

    @staticmethod
    def hash(block):
        pass

    @staticmethod
    def merkle_root(transactions):
        pass


