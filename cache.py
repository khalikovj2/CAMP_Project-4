class CacheLine:
    def __init__(self):
        self.valid = False
        self.tag = None
        self.data = [0] * 16  # 64 bytes = 16 words
        self.last_used = 0

class Cache:
    def __init__(self, size, line_size, associativity, write_policy):
        self.size = size
        self.line_size = line_size
        self.associativity = associativity
        self.write_policy = write_policy
        self.sets = size // (line_size * associativity)
        self.cache = [[CacheLine() for _ in range(associativity)] for _ in range(self.sets)]
        self.cycle = 0
        self.hit_count = 0
        self.miss_count = 0

    def _index_and_tag(self, address):
        line_offset = self.line_size.bit_length() - 1
        index_bits = self.sets.bit_length() - 1
        index = (address >> line_offset) & ((1 << index_bits) - 1)
        tag = address >> (line_offset + index_bits)
        return index, tag

    def read_word(self, address, memory):
        self.cycle += 1
        index, tag = self._index_and_tag(address)
        set_lines = self.cache[index]

        for line in set_lines:
            if line.valid and line.tag == tag:
                self.hit_count += 1
                line.last_used = self.cycle
                word_offset = (address % self.line_size) // 4
                return line.data[word_offset]

        self.miss_count += 1
        victim = min(set_lines, key=lambda l: l.last_used if l.valid else -1)
        block_addr = address - (address % self.line_size)
        for i in range(16):
            victim.data[i] = memory.read_word(block_addr + i * 4)
        victim.valid = True
        victim.tag = tag
        victim.last_used = self.cycle
        word_offset = (address % self.line_size) // 4
        return victim.data[word_offset]

    def access(self, instr, memory):
        return 1000 if self.miss_count > 0 else 1
