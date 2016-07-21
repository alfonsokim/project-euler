from itertools import permutations as perms

# ============================================================
def solve():
    """
    """
    permutations = sorted([''.join(p) 
                    for i, p in enumerate(perms(str(d) for d in range(10)))
                    if i < 1000000])
    return permutations[-1]

# ============================================================
if __name__ == '__main__':
    print solve()