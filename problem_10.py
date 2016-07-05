
import utils

# ============================================================
def solve():
    """
    """
    tester = utils.DynamicPrimalTester()
    is_prime = tester.is_prime
    generator = utils.int_generator(start=1, stop=2000000)
    # return sum(filter(lambda x: t(x), range(1, 2000001)))
    return sum(x for x in generator if is_prime(x))

# ============================================================
if __name__ == '__main__':
    """
    """
    print solve()
