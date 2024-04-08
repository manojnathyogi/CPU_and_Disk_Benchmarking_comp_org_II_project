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
