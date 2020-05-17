##########################
# Name: Alex Faucheux
# Language: Python 3
##########################

import sys


# XOR a and b bytes iterated from byte pairs created with zip
def byte_xor(bin1, bin2):
    return bytes([a ^ b for a, b in zip(bin1, bin2)])


# Read file in binary
key_bytes = open('key', 'rb').read()
data_bytes = sys.stdin.buffer.read()
result = byte_xor(data_bytes, key_bytes)
sys.stdout.buffer.write(result)
