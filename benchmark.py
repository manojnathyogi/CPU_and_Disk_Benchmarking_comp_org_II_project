import time
import os
import numpy as np

def int_operations_benchmark():
    print("Starting 32-bit integer operations...")
    start_time = time.time()
    # 1010 additions
    a = 1
    for _ in range(1010):
        a += 1
    # 5 x 10^9 multiplications
    b = 1
    for _ in range(5000000000):
        b *= 2
        b %= 2147483647  # Keep it within the 32-bit integer range
    # 2 x 10^9 divisions
    c = 10000000000
    for _ in range(2000000000):
        c //= 2
    end_time = time.time()
    total_time = end_time - start_time
    print(f"32-bit Integer Operation Benchmark: {total_time:.2f} seconds")

def float_operations_benchmark():
    print("Starting 64-bit floating point operations...")
    start_time = time.time()
    # 1010 additions
    a = 1.0
    for _ in range(1010):
        a += 1.0
    # 5 x 10^9 multiplications
    b = 1.0
    for _ in range(5000000000):
        b *= 1.0000001  # Small multiplication to avoid infinity
    # 2 x 10^9 divisions
    c = 1e10
    for _ in range(2000000000):
        c /= 2.0
    end_time = time.time()
    total_time = end_time - start_time
    print(f"64-bit Floating Point Operation Benchmark: {total_time:.2f} seconds")

def memory_benchmark():
    print("Starting memory operations...")
    n = 5000000000
    array = np.zeros(n, dtype=np.uint8)
    start_time = time.time()
    # Reading from array
    sum = 0
    for i in range(n):
        sum += array[i]
    # Writing to array
    for i in range(n):
        array[i] = 1
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Memory Benchmark: {total_time:.2f} seconds")

def hard_drive_benchmark(file_path, file_size, block_size):
    print(f"Starting hard drive benchmark with block size {block_size}...")
    # Create a test file
    with open(file_path, "wb") as f:
        f.write(os.urandom(file_size))
    start_time = time.time()
    # Read the file
    with open(file_path, "rb") as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
    # Write to the file
    with open(file_path, "wb") as f:
        for _ in range(file_size // block_size):
            f.write(os.urandom(block_size))
    end_time = time.time()
    os.remove(file_path)  # Clean up the file
    total_time = end_time - start_time
    print(f"Hard Drive Benchmark ({block_size} bytes per op): {total_time:.2f} seconds")

if __name__ == "__main__":
    int_operations_benchmark()
    float_operations_benchmark()
    memory_benchmark()
    hard_drive_benchmark("testfile1.bin", 1000000000, 100)  # 100 bytes per operation
    hard_drive_benchmark("testfile2.bin", 1000000000, 10000)  # 10000 bytes per operation