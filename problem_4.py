

# ============================================================
def solve():
    """
    """
    def next_palindrome():
        for i in range(999, 99, -1):
            for j in range(999, 99, -1):
                prod = i * j
                s = str(prod)
                if s == s[::-1]:
                    yield prod
    return str(max(next_palindrome()))


# ============================================================
if __name__ == '__main__':
    """
    """
    print solve()