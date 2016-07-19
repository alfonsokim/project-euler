
# ============================================================
def solve():
    """
    """
    letter_index = dict((d, i+1) for i, d in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    lines = [l.replace('"', '') for l in open('p022_names.txt').readlines()]
    names = sorted(''.join(lines).split(','))
    sum_score = 0
    for idx, name in enumerate(names):
        sum_score += (idx+1) * (sum(letter_index[c] for c in name))
    return sum_score


# ============================================================
if __name__ == '__main__':
    """
    """
    print solve()