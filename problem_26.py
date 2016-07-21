
# ============================================================
def period(n):
    """ Divide entre x*=10 hasta encontrar un numero en el
        denominador que se repite.
        Basado en que el periodo no puede ser algo como
        112233 o 1231234. Es decir, que cuando se repite un
        numero en el denominador es que ya inicio la siguiente
        secuencia
    """
    memory = {}
    x, i = 1, 0
    while x not in memory:
        memory[x] = i
        x = (x * 10) % n
        i += 1
    return i - memory[x]

# ============================================================
def solve():
    """
    """
    return max(range(1, 1000), key=period)

# ============================================================
if __name__ == '__main__':
    print solve()