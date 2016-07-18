# ============================================================
def solve():
    """
    """
    from datetime import date # <- lets cheat
    def next_first_day():
        '''
        '''
        for year in range(1901, 2001):
            for month in range(1, 13):
                yield date(year, month, 1)
    
    return sum(1 if d.weekday() == 6 else 0 for d in next_first_day())

# ============================================================
if __name__ == '__main__':
    """
    """
    print solve()