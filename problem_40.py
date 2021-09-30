# =======================================================================================
def solve():
    # Use the brute force
    decimal_part = ''
    start, end, step = 1, 11, 10
    while len(decimal_part) < 1000000: # 1000000:
        decimal_part += ''.join([str(v) for v in range(start, end)])
        start, end = end, end + step
    return reduce(lambda x, y: x*y, [int(decimal_part[10**i-1]) for i in range(7)])


# =======================================================================================
if __name__ == '__main__':
    print(solve())
