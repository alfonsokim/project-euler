
def fibonacci(num):
    """ Muy bonito, pero no se usa por la naturaleza del problema
        https://projecteuler.net/problem=2
    """
    memory = {0: 1, 1: 1}
    result = 0
    def fib(a):
        if a in memory:
            return memory[a]
        memory[a] = fib(a - 1) + fib(a - 2)
        return memory[a]
    return fib(num)



if __name__ == '__main__':
    """
    """
    x, y, result = 1, 2, 0
    while x < 4*10**6:
        if x % 2 == 0: result += x
        x, y = y, x + y
    print result