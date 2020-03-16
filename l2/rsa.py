import random
import sys


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def multiplicative_inversion(a, b):
    s = 0
    old_s = 1
    r = b
    old_r = a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient*r
        old_s, s = s, old_s - quotient*s

    return old_s


def miller_rabin(n):
    if n == 0 or n == 1:
        return False

    d = n-1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1

    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i*d, n) == n-1:
                return False
        return True

    for _ in range(8):
        a = random.randrange(2, n)
        if trial_composite(a):
            return False

    return True


def calculate_keys(p, q):
    n = p*q
    phi = (p-1)*(q-1)

    g = 0
    while g != 1:
        d = random.randrange(2, phi-1)
        g = gcd(d, phi)

    e = multiplicative_inversion(d, phi)

    return ((e, n), (d, n))


def encode_char(char, key):
    e, n = key
    return str(pow(ord(char), e, n))


def decode_char(char, key):
    d, n = key
    return chr(pow(int(char), d, n))

def encrypt(message, key):
    return '|'.join(encode_char(ch, key) for ch in message)

def decrypt(message, key):
    return ''.join(decode_char(ch, key) for ch in message.split('|'))


def generate_keys(bits: int):
    low = 2**(bits-1)
    high = 2**bits

    p = 0
    while not miller_rabin(p):
        p = random.randrange(low, high)

    q = 0
    while not miller_rabin(q):
        q = random.randrange(low, high)

    pub, prv = calculate_keys(p, q)

    with open('key.pub', 'w+') as f:
        f.write(hex(pub[0]))
        f.write('\n')
        f.write(hex(pub[1]))

    with open('key.prv', 'w+') as f:
        f.write(hex(prv[0]))
        f.write('\n')
        f.write(hex(prv[1]))


if __name__ == "__main__":
    mode = sys.argv[1]

    if mode == '--gen-keys':
        generate_keys(int(sys.argv[2]))
    elif mode == '--encrypt':
        with open('key.pub', 'r') as f:
            message = sys.argv[2]
            key = [int(n, 16) for n in f.read().split()]
            print(encrypt(message, key))
    elif mode == '--decrypt':
        with open('key.prv', 'r') as f:
            message = sys.argv[2]
            key = [int(n, 16) for n in f.read().split()]
            print(decrypt(message, key))
