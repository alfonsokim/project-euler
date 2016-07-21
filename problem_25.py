# ============================================================
def next_fibonacci():
    """
    """
    yield 1
    yield 1
    memory = {0: 1, 1: 1}
    i = 2
    while True:
        next_fib = memory[i-1] + memory[i-2]
        memory[i] = next_fib
        yield next_fib
        i += 1


# ============================================================
def solve():
    """
    """
    for i, fib in enumerate(next_fibonacci()):
        if len(str(fib)) == 1000:
            return i+1

# ============================================================
if __name__ == '__main__':
    print solve()