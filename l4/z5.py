from cmath import exp
from math import pi

def omega(k, n):
    return exp(-2j*k*pi/n)

def dft(x, n):
    return [sum(x[i]*omega(i*k, n) if i < len(x) else 0 for i in range(n)) for k in range(n)]

def idft(x, n):
    return [int(round(sum(x[i]*omega(-i*k, n) if i < len(x) else 0 for i in range(n)).real)/n) for k in range(n)]


class FastBigNum:
    def __init__(self, num):
        self.num = list(map(int, num))

    def __mul__(self, other):
        n = max(len(self.num), len(other.num))

        x_star = dft(self.num[::-1], 2*n)
        y_star = dft(other.num[::-1], 2*n)
        z_star = [x_star[i]*y_star[i] for i in range(2*n)]
        z = idft(z_star, 2*n)

        return FastBigNum(''.join(map(str, z[::-1])).lstrip('0'))

    def __repr__(self):
        return ''.join(map(str, self.num))


# A = '13123122312321312312312231231231231212331233231349'
# B = '12123123112231231213123312321321231231112323123231'

A = '135'
B = '210'

a = FastBigNum(A)
b = FastBigNum(B)

result1 = a*b#*a*b
print(result1)

a = int(A)
b = int(B)

result2 = a*b#*a*b
print(result2)

print(int(str(result1)) == result2)
        



