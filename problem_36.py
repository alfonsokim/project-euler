
# =======================================================================================
def is_palindrome(a_str):
    return a_str == a_str[::-1]

# =======================================================================================
def solve():
    a_sum = 0
    for i in range(1, 1000000, 2):
        both_palindromes = is_palindrome(format(i, 'b')) and is_palindrome(str(i))
        a_sum += i if both_palindromes else 0
    print a_sum


# =======================================================================================
if __name__ == '__main__':
    solve()