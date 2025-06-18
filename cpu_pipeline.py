class CPU:
    def __init__(self, memory, cache):
        self.memory = memory
        self.cache = cache
        self.registers = [0] * 32
        self.pc = 0x0
        self.cycle_count = 0
        self.mem_access_count = 0
        self.reg_op_count = 0
        self.branch_count = 0
        self.branch_taken_count = 0

    def reset(self):
        self.registers = [0] * 32
        self.registers[31] = 0xFFFFFFFF  # $ra
        self.pc = 0x0
        self.cycle_count = 0
        self.mem_access_count = 0
        self.reg_op_count = 0
        self.branch_count = 0
        self.branch_taken_count = 0

    def run(self):
        while self.pc != 0xFFFFFFFF:
            instruction = self.cache.read_word(self.pc, self.memory)
            self.cycle_count += 1
            self.execute(instruction)

    def execute(self, instr):
        opcode = (instr >> 26) & 0x3F
        if opcode == 0x00:  # R-type
            self.reg_op_count += 1
        elif opcode in [0x23, 0x2B]:  # lw or sw
            self.mem_access_count += 1
            self.cycle_count += self.cache.access(instr, self.memory)
        elif opcode in [0x04, 0x05]:  # beq or bne
            self.branch_count += 1
            taken = self.simulate_branch(instr)
            if taken:
                self.branch_taken_count += 1
        self.pc += 4

    def simulate_branch(self, instr):
        return False  # Simplified for base emulator

    def calculate_amat(self):
        if self.mem_access_count == 0:
            return 1.0
        hit_time = 1
        miss_penalty = 1000
        hit_rate = self.cache.hit_count / (self.cache.hit_count + self.cache.miss_count)
        return hit_time + (1 - hit_rate) * miss_penalty
