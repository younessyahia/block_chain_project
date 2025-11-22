import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        content = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(content.encode()).hexdigest()

    def mine_block(self, difficulty="0000"):
        print(f"Mining block {self.index} ...")
        while not self.hash.startswith(difficulty):
            self.nonce += 1
            self.hash = self.calculate_hash()   
        print(f"Block mined! Hash = {self.hash}\n")

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = "0000"  

    def create_genesis_block(self):
        return Block(0, time.strftime("%Y-%m-%d %H:%M:%S")
, "Genesis Block", "0")

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, data):
        last_block = self.get_last_block()
        new_block = Block(len(self.chain), time.strftime("%Y-%m-%d %H:%M:%S")
, data, last_block.hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
            if not current.hash.startswith(self.difficulty):
                return False

        return True

my_chain = Blockchain()

my_chain.add_block("Younes’ first block")
my_chain.add_block("Ibrahim’ second block")


for block in my_chain.chain:
    print("----------------------------")
    print("Index:", block.index)
    print("Timestamp:", block.timestamp)
    print("Data:", block.data)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)

print("\nIs chain valid?", my_chain.is_chain_valid())

my_chain.chain[1].data= "edited data"


print("Is chain valid after tampering?", my_chain.is_chain_valid())
