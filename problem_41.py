import itertools
from utils import PrimalTester

# =======================================================================================
"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?
"""
def solve():
    tester = PrimalTester()
    all_digits = '987654321'
    for digits in [all_digits[i:] for i in range(len(all_digits))]:
        for c, pandigital_str in enumerate(itertools.permutations(digits)):
            if int(pandigital_str[-1]) % 2 == 0:
                continue
            pandigital = int(''.join(pandigital_str))
            if tester.is_prime(pandigital):
                return pandigital
            if c and c % 1000 == 0:
                print('%i tests with %s digits' % (c, digits))


# =======================================================================================
if __name__ == '__main__':
    print(solve())
