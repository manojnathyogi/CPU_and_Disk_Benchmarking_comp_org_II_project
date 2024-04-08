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
