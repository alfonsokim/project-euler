
# =============================================================================
def solve():
    """ Super fuerza bruta
    """
    da_sum = 0
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    amount = 200
    ways = [1] + [0] * amount
    for coin in coins:
    	for j in range(coin, amount):
    		print j
    		ways[j] += ways[j-coin]
    return ways[amount]


# =============================================================================
if __name__ == '__main__':
    print solve()