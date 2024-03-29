import time

# ============================================================
class DynamicPrimalTester():

    # --------------------------------------------------------
    def __init__(self):
        """ Tester for primality of an integer number
            Uses Dynamic Programming to keep track of tested
            numbers
        """
        self.memory = {
            0: False, 
            1: False, 
            2: True, 
            3: True, 
            4: False, 
            5: True, 
            6: False, 
            7: True, 
            8: False
        }
        self.num_tests = 0
        self.hits = 0

    # --------------------------------------------------------
    def is_prime(self, x):
        """ Returns True if x is prime, False otherwhise
        """
        if x < 0: return False
        self.num_tests += 1
        if x % 2 == 0:
            self.memory[x] = False
            return False
        if x in self.memory:
            # self.hits += 1
            return self.memory[x]
        xsqrt = int(x ** 0.5)
        for i in range(3, xsqrt + 1, 2):
            if x % i == 0:
                # print '%i es multiplo de %i' % (x, i)
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


# ============================================================
PrimalTester = DynamicPrimalTester

# ============================================================
def proper_divisors(number, stop=None):
    """
    """
    # i, n = 1, (number // 2) + 1
    yield 1
    i, n = 2, int(number ** 0.5) + 1
    while i < stop or i < n:
        if number % i == 0:
            yield i
            if i != number // i: 
                yield number // i
        i += 1


# ============================================================
def time_it(da_func):
    """
    """
    def wrap(*args, **kwargs):
        time1 = time.time()
        ret_value = da_func(*args, **kwargs)
        time2 = time.time()
        print('[%s]: %0.4f ms' % (da_func.func_name, (time2 - time1) * 1000.0))
        return ret_value
    return wrap

