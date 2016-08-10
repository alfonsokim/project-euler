from utils import PrimalTester
from collections import defaultdict

tester = PrimalTester()

# ============================================================
def count_primes(a, b):
    """ Cuenta el numero de primos en la combinacion de a y b
    """
    i = 0
    while True:
        if not tester.is_prime((i * i) + (i * a) + b):
            return i
        i += 1

# ============================================================
def solve():
    """
    """
    range_a, range_b = range(-999, 1000), range(2, 1000)
    num_primes_a_b = [(count_primes(a, b), a*b) for a in range_a for b in range_b]
    return max(num_primes_a_b, key=lambda t: t[0])[1]


# ============================================================
if __name__ == '__main__':
    print solve()
