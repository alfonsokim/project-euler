
# ============================================================
def solve():
    """
    """
    memory = {1: 2}
    def collatz(N, n, count):
        """ Iba a usar memoizacion, pero no me salio =(
        """
        n = n // 2 if n % 2 == 0 else (n * 3) + 1
        count += 1
        if n == 1:
            return (N, count)
        else: 
            return collatz(N, n, count)

    return max([collatz(i, i, 1) for i in range(2, 1000000)], key=lambda t: t[1])[0]


# ============================================================
if __name__ == '__main__':
    """
    """
    print solve()