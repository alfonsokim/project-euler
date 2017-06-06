
from utils import PrimalTester

# =======================================================================================
def decompose(num, direction=1):
    yield num
    str_num = str(num)
    while len(str_num) > 1:
        str_num = str_num[1:] if direction == 1 else str_num[:-1]
        yield int(str_num)

# =======================================================================================
def solve():
    tester = PrimalTester()
    special_primes = []
    i = 11
    while len(special_primes) < 11:
        left = [tester.is_prime(n) for n in decompose(i)]
        right = [tester.is_prime(n) for n in decompose(i, -1)]
        if all(left) and all(right):
            special_primes.append(i)
        i += 1
    print sum(special_primes)


# =======================================================================================
if __name__ == '__main__':
    solve()