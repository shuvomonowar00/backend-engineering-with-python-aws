'''
    Count digits from numbers
'''

import math


def count_digits(num: int) -> int:
    digits = int(math.log10(num)) # O(1)
    return digits+1


if __name__ == '__main__':
    num = int(input('Enter number: '))
    print(count_digits(num))


# Time Complexity -> O(1)
