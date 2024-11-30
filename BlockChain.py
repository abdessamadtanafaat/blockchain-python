from hashlib import sha512  # Import the sha512 hashing algorithm from the hashlib module

# Define the hashing function
def hachage(*args):
    """
    Generates a SHA-512 hash by concatenating all arguments.
    :param args: The inputs to be hashed.
    :return: The resulting hash as a hexadecimal string.
    """
    hach = sha512()  # Create a new SHA-512 hash object
    text = "".join(map(str, args))  # Concatenate all arguments into a single string
    hach.update(text.encode('utf-8'))  # Encode the string as UTF-8 and update the hash object
    return hach.hexdigest()  # Return the hexadecimal digest of the hash


# Define the Block class
class Block:
    def __init__(self, data, numero=0):
        """
        Initialize a block with its data and optional attributes.
        :param data: The data stored in the block (e.g., transactions).
        :param numero: The block's index in the chain (default is 0).
        """
        self.data = data  # Data contained in the block
        self.numero = numero  # Block index
        self.nonce = 0  # Counter used for proof-of-work
        self.hash_precedent = "0" * 128  # Hash of the previous block (default is 128 zeros)

    def hash(self):
        """
        Compute the hash of the block.
        :return: The block's hash as a string.
        """
        return str(hachage(
            self.numero,  # Block index
            self.hash_precedent,  # Hash of the previous block
            self.data,  # Block data
            self.nonce  # Proof-of-work nonce
        ))

    def __str__(self):
        """
        Define how to represent the block as a string.
        :return: A formatted string representation of the block.
        """
        return (
            f"Numero Block: {self.numero}\n"
            f"Hash: {self.hash()}\n"
            f"Precedent: {self.hash_precedent}\n"
            f"Data: {self.data}\n"
            f"Nonce: {self.nonce}\n"
        )


# Define the Blockchain class
class Blockchain:
    def __init__(self, chain=None, difficulte=5):
        """
        Initialize the blockchain.
        :param chain: A list to hold the blocks in the chain (default is an empty list).
        :param difficulte: The proof-of-work difficulty (default is 5).
        """
        if chain is None:
            chain = []  # Initialize an empty list if no chain is provided
        self.chain = chain  # The chain of blocks
        self.difficulte = difficulte  # Number of leading zeros required in the hash
        self.nombre_block = 0  # Number of blocks in the chain

    def __str__(self):
        """
        Define how to represent the blockchain as a string.
        :return: A string representation of all blocks in the chain.
        """
        return "\n".join(str(block) for block in self.chain)  # Concatenate all block representations

    def miner(self, block):
        """
        Mine a new block by finding a hash that satisfies the difficulty requirement.
        :param block: The block to be mined.
        """
        try:
            # Set the hash of the previous block
            block.hash_precedent = self.chain[self.nombre_block - 1].hash()
        except IndexError:
            # If the chain is empty, this is the genesis block
            pass

        # Increment the block counter
        self.nombre_block += 1
        block.numero = self.nombre_block  # Assign the block's index

        while True:
            # Check if the hash starts with the required number of leading zeros
            if block.hash().startswith("0" * self.difficulte):
                self.chain.append(block)  # Add the block to the chain
                break  # Exit the loop once the block is mined
            else:
                block.nonce += 1  # Increment the nonce and try again

    def isValid(self):
        """
        Verify the integrity of the blockchain.
        :return: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            # Get the hash of the previous block and the stored previous hash
            _courant = self.chain[i - 1].hash()
            _precedent = self.chain[i].hash_precedent

            # Check if the current block's previous hash matches the previous block's hash
            if _courant != _precedent:
                return False  # Blockchain is invalid
        return True  # Blockchain is valid


# Main function to test the blockchain
def main():
    # Initialize a blockchain
    blockchain = Blockchain()
    # Example database of transactions
    database = ["transaction1", "transaction2", "transaction3", "transaction4"]

    # Mine a block for each transaction
    for data in database:
        blockchain.miner(Block(data))

    # Print the entire blockchain
    print(blockchain)
    print("Is blockchain valid? " + str(blockchain.isValid()) + "\n")

    # Simulate tampering with the blockchain
    blockchain.chain[2].data = "hacker"  # Modify data in a block

    # Check if the blockchain is still valid
    print("Is blockchain valid? " + str(blockchain.isValid()) + "\n")
    # Print the blockchain after tampering
    print(blockchain)


# Run the main function
main()
