import utils

# ============================================================
@utils.time_it
def solve():
    """
    """
    pd = utils.proper_divisors
    problem_range = set(range(1, 28123))
    abundants = [n for n in problem_range if sum(d for d in pd(n)) > n]
    for a in abundants:
        for b in abundants:
            if a + b in problem_range:
                problem_range.remove(a+b)
    return sum(problem_range)

# ============================================================
if __name__ == '__main__':
    print solve()