# ============================================================
def next_triangle(num_triangles=None, stop=None):
    """
    """
    forever = None == num_triangles == stop
    i, triangle = 1, 0
    while forever or (i <= num_triangles or triangle < stop):
        i, triangle = i+1, triangle+i
        yield triangle


# ============================================================
def factors(n):
    """
    """
    da_factors = []
    for f in [f for f in range(1, int(n**0.5) + 1) if n % f == 0]:
        da_factors.extend([f, n//f])
    return set(da_factors)


# ============================================================
def solve():
    """
    """
    for t in next_triangle():
        if len(factors(t)) >= 500:
            return t

# ============================================================
if __name__ == '__main__':
    """
    """
    print solve()