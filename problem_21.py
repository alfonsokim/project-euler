
# ============================================================
def solve():
    """
    """
    def amicable(number):
        '''
        '''
        return sum(i for i in range(1, (number // 2) + 1) if number % i == 0)

    accumulate = 0
    for a in range(1, 10000):
        b = amicable(a)
        if a != b and a == amicable(b):
            accumulate += a

    return accumulate

# ============================================================
if __name__ == '__main__':
    """
    """
    print solve()