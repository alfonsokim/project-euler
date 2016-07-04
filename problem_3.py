import itertools

# ============================================================
def is_prime(x, memory):
    """ Not used, taking too long
    """
    if x in memory:
        return memory[x]
    xsqrt = int(x ** 0.5)
    for i in range(3, xsqrt + 2, 2):
        if i in memory:
            return memory[i]
        if x % 2 == 0 or x % i == 0:
            memory[i] = False
            return False
    memory[x] = True
    return True

# ============================================================
def minimum_prime_factor(num):
    """
    """
    xsqrt = int(num ** 0.5)
    for i in itertools.count(3, 2):
        if i >= xsqrt: # condicion de salida
            return num
        if num % i == 0:
            return i


# ============================================================
def solve(num):
    """
    """
    current_prime = num
    while current_prime <= num:
        current_prime = minimum_prime_factor(num)
        num /= current_prime
    return current_prime

# ============================================================
if __name__ == '__main__':
    print solve(600851475143)
