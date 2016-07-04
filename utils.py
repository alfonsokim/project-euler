
# ============================================================
class DynamicPrimalTester():

    # --------------------------------------------------------
    def __init__(self):
        """
        """
        self.memory = {0: False, 1: True, 2: True, 3: True, 4: False, 
                       5: True, 6: False, 7: True, 8: False}
        self.num_tests = 0
        self.hits = 0

    # --------------------------------------------------------
    def test(self, x):
        """
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
    """
    """
    def hit_rate(self):
        return self.hits / float(self.num_tests)

    # --------------------------------------------------------
    """
    """
    def miss_rate(self):
        return (self.num_tests - self.hits) / float(self.num_tests)




