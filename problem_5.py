
def gcd(a, b):
    # ============================================================
    """
    """
    while b:
        a, b = b, a % b
    return a

# ============================================================
def solve():
    """
    """
    current_min = 1
    for i in range(1, 21):
        current_min *= i / gcd(i, current_min)
    return str(current_min)


# ============================================================
if __name__ == '__main__':
    """
    """
    print solve()