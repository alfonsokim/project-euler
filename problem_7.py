import utils

# ============================================================
def solve():
    """
    """
    tester = utils.DynamicPrimalTester()
    i = 0
    num_primes = 0
    while num_primes <= 10001:
        i += 1
        if tester.test(i):
            num_primes += 1
    print 'hit rate: %.4f' % tester.hit_rate()
    print 'miss rate: %.4f' % tester.miss_rate()
    return str(i)


# ============================================================
if __name__ == '__main__':
    """
    """
    print solve()