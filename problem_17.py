
# ============================================================
def in_english(number):
    """
    """
    ZERO_ORDER = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 
                  'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    FIRST_ORDER = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    SECOND_ORDER = ['']
    if number < 20:
        return ZERO_ORDER[number]
    if number < 100:
        return ' '.join([FIRST_ORDER[number // 10], in_english(number % 10)])
    if number < 1000:
        hundreds = '%s hundred' % in_english(number // 100)
        dozens = 'and %s' % (in_english(number % 100)) if number % 100 > 0 else ''
        return ' '.join([hundreds, dozens]).strip()
    if number == 1000:
        aanndd = ' and ' if number % 1000 > 0 else ''
        return 'one thousand%s%s' % (aanndd, in_english(number % 1000))
    raise Exception()

# ============================================================
def solve():
    """
    """
    return len(''.join([in_english(i).replace(' ', '') for i in range(1, 1001)]))

# ============================================================
if __name__ == '__main__':
    """
    """
    print solve()
