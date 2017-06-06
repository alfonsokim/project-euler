import itertools
from collections import defaultdict

# =======================================================================================
def next_triangle(max_perimeter):
    for a, b in itertools.product(range(1, max_perimeter), range(1, max_perimeter)):
        c = ((a*a) + (b*b)) ** 0.5
        if c.is_integer() and (a + b + c) <= max_perimeter:
            yield a, b, int(c)
        

# =======================================================================================
def solve():
    solutions = defaultdict(list)
    for sides in next_triangle(1000):
        solutions[sum(sides)].append(sides)
    max_solutions = sorted(solutions.items(), key=lambda e: len(e[1]) * -1)[0]
    return max_solutions[0]


# =======================================================================================
if __name__ == '__main__':
    print solve()