Description:You will develop five benchmarks. The details of the benchmarks are as follows:

32-bit Integer operation benchmark (reference time: 100 seconds)
-> 1010 additions (of integer constants)
-> 5 × 109 multiplication (of integer constants)
-> 2 × 109 division (of integer constants)

64-bit Floating point operation benchmark (reference time: 100 seconds)
-> Same as integer, use double precision floating point numbers instead of integer.

Memory benchmark (reference time: 100 seconds)
-> Read from 5 × 109 different array elements, 4 bytes each time
-> Write to 5 × 109 different array elements, 4 bytes each time

Hard drive benchmark 1 (reference time: 250 seconds)
-> Read a whole file of 109 bytes, 100 bytes each time
-> Write 109 bytes to a file, 100 bytes each time

Hard drive benchmark 2 (reference time: 10 seconds)
-> Read a whole file of 109 bytes, 10000 bytes each time
-> Write 109 bytes to a file, 10000 bytes each time

Each benchmark will output the total execution time of the benchmark. Note that the benchmark must NOT do any operations other than what is specified above. The output should be done only once at the end of the program.
