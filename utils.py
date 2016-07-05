
# ============================================================
class DynamicPrimalTester():

    # --------------------------------------------------------
    def __init__(self):
        """ Tester for primality of an integer number
            Uses Dynamic Programming to keep track of tested
            numbers
        """
        self.memory = {0: False, 1: False, 2: True, 3: True, 4: False, 
                       5: True, 6: False, 7: True, 8: False}
        self.num_tests = 0
        self.hits = 0

    # --------------------------------------------------------
    def is_prime(self, x):
        """ Returns True if x is prime, False otherwhise
        """
        self.num_tests += 1
        if x in self.memory:
            self.hits += 1
            return self.memory[x]
        xsqrt = int(x ** 0.5)
        for i in range(3, xsqrt + 1, 2):
            if x % 2 == 0 or x % i == 0:
                self.memory[x] = False
                return False
        self.memory[x] = True
        return True

    # --------------------------------------------------------
    """ FIX THIS!
    """
    def hit_rate(self):
        return self.hits / float(self.num_tests)

    # --------------------------------------------------------
    """ FIX THIS!
    """
    def miss_rate(self):
        return (self.num_tests - self.hits) / float(self.num_tests)


# ============================================================
def int_generator(start=0, stop=None, step=1):
    """ Overcome that range creates the list before iteration =S
    """
    i = 0
    while i < stop:
        yield i
        i += step

