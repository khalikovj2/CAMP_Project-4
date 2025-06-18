class Memory:
    def __init__(self):
        self.data = {}

    def load_binary(self, filepath):
        with open(filepath, "rb") as f:
            byte_addr = 0
            while byte := f.read(4):
                word = int.from_bytes(byte, byteorder="big")
                self.data[byte_addr] = word
                byte_addr += 4

    def read_word(self, address):
        return self.data.get(address, 0)

    def write_word(self, address, value):
        self.data[address] = value

