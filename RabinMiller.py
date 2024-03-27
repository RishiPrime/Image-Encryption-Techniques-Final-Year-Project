import random
import ModularArithmetic as mod

def is_probably_prime(n):
    tests = max(128, n.bit_length())
    for i in range(tests):
        rand = random.randint(1,n-1)
        return 1 in mod.binary_exponent(rand, n-1, n)

def generate_prime(bitlen=128):
    n = random.getrandbits(bitlen) | 1<<(bitlen-1) | 1
    while not is_probably_prime(n):
        n = random.getrandbits(bitlen) | 1<<(bitlen-1) | 1
    return n