
# ============================================================
def solve():
    """
    """
    memory = {}
    def factorial(n):
        '''
        '''
        if n in memory:
            return memory[n]
        if n == 1:
            return 1
        fact = n * factorial(n - 1)
        memory[factorial] = fact
        return fact
        
    return sum(int(d) for d in list(str(factorial(100))))

# ============================================================
if __name__ == '__main__':
    """
    """
    print solve()