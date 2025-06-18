
 Pipelined MIPS Emulator with Cache Simulation

 Overview

This project implements a software simulation of a pipelined MIPS CPU integrated with a configurable cache subsystem. The primary goal is to analyze how cache structure and policies impact memory access performance and overall processor execution efficiency.



Project Structure

* `memory.py`
  Simulates the main memory system. Loads the input MIPS binary into a large memory array and provides byte-addressable read/write operations.

* `cache.py`
  Implements a CPU cache simulator with configurable parameters including cache size, set-associativity, replacement policy (LRU), and write policy (write-back/write-through). Tracks cache hits, misses (cold and conflict), and simulates corresponding cache and memory latencies.

* `cpu-pipeline.py`
  Simulates a pipelined MIPS processor with standard five pipeline stages: instruction fetch, decode, execute, memory access, and write-back. Handles pipeline hazards (stalls, flushes) and interacts with the cache module for memory operations.

* `main.py`
  The program entry point. Initializes the memory, cache, and CPU pipeline modules, loads the input binary program, runs the simulation loop until program termination, and outputs detailed execution statistics and results.

* `input.bin`
  Example MIPS binary input file loaded into memory for simulation testing.

 Features

* Configurable Cache:
  Supports cache sizes of 64, 128, and 256 bytes.

* Flexible Associativity:
  Allows direct-mapped, 2-way, 4-way, and 8-way set associativity.

* LRU Replacement Policy:
  Implements Least Recently Used algorithm for cache line replacement.

* Write Policies:
  Supports both write-back and write-through cache write policies.

* Latency Simulation:
  Cache hit latency is modeled as 1 CPU cycle, memory access latency as 1000 CPU cycles.

* Program Termination Detection:
  Simulation halts when Program Counter (PC) reaches `0xFFFFFFFF`.

* Comprehensive Statistics:
  Tracks total execution cycles, instruction counts, branch counts (taken/untaken), cache hits, misses (cold and conflict), and calculates Average Memory Access Time (AMAT).



 Usage Instructions

1. Configure Parameters:
   Adjust cache configuration parameters (size, associativity, write policy) and specify the input binary file path within `main.py`.

2. Run the Simulator:
   Execute the simulation with Python 3:
Commmand: python3 main.py
3. View Output:
   After simulation completes, review the printed execution statistics and computed result from the MIPS program.



