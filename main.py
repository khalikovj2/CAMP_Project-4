from memory import Memory
from cache import Cache
from cpu_pipeline import CPU

def main():
    CACHE_SIZE = 256
    CACHE_LINE_SIZE = 64
    CACHE_ASSOCIATIVITY = 4
    WRITE_POLICY = 'write-back'

    memory = Memory()
    cache = Cache(size=CACHE_SIZE, line_size=CACHE_LINE_SIZE,
                  associativity=CACHE_ASSOCIATIVITY,
                  write_policy=WRITE_POLICY)
    cpu = CPU(memory, cache)

    binary_file = 'input.bin'
    memory.load_binary(binary_file)
    cpu.reset()
    cpu.run()

    print(f"0x{cpu.registers[2]:08X}")
    print(f"{cpu.cycle_count}")
    print(f"{cpu.mem_access_count}")
    print(f"{cpu.reg_op_count}")
    print(f"{cpu.branch_count}/{cpu.branch_taken_count}")
    print(f"{cache.hit_count}")
    print(f"{cache.miss_count}")
    print(f"{cpu.calculate_amat():.2f}")

if __name__ == "__main__":
    main()
