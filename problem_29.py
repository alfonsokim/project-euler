
# =============================================================================
def solve():
    """
    """
    range_a, range_b = range(2, 101), range(2, 101)
    return len(set([a ** b for a in range_a for b in range_b]))


# =============================================================================
if __name__ == '__main__':
    print solve()