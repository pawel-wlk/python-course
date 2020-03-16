import sys

ENCODING = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'


def encode(file: str):
    result = ''
    with open(file, 'rb') as f:
        chunk = f.read(3)
        while chunk:
            if len(chunk) != 3:
                chunk += int(0).to_bytes(3-len(chunk), 'big')
            bitstring = bin(int(chunk.hex(), base=16))[2:].rjust(24, "0")
            codes = (bitstring[i:i+6] for i in range(0, 24, 6))

            for code in codes:
                result += ENCODING[int(code, base=2)]

            chunk = f.read(3)

    return result


def decode(file: str):
    result = bytes()
    with open(file, 'r') as f:
        chunk = f.read(4)
        while chunk:
            chunk_bitstring = ''
            for char in chunk:
                char_number = ENCODING.index(char)
                chunk_bitstring += bin(char_number)[2:].rjust(6, '0')
            outchar_bistrings = (chunk_bitstring[i:i+8]
                                 for i in range(0, 24, 8))
            for bitstring in outchar_bistrings:
                print(bitstring)
                byte = int(bitstring, base=2).to_bytes(1, 'big')
                if byte != b'\x00':
                    result += byte
            chunk = f.read(4)

    return result


if __name__ == '__main__':
    if sys.argv[1] == '--encode':
        print(encode(sys.argv[2]), end='')
    elif sys.argv[1] == '--decode':
        print(decode(sys.argv[2]), end='')
