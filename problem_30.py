
# =============================================================================
def solve():
    """ Super fuerza bruta
    """
    da_sum = 0
    for n in range(2, 10000000):
        exp_digits = map(lambda d: d**5, [int(d) for d in str(n)])
        da_sum += n if n == sum(exp_digits) else 0
    return da_sum


# =============================================================================
if __name__ == '__main__':
    print solve()
