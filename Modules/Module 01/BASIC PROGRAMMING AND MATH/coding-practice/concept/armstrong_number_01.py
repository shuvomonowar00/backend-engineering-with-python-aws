'''
    What is Armstrong number?
    --> A number is an Armstrong number if the sum of the cube of each of its digits is the same
        as the given number.
'''

import math


def armstrong_number(num: int) -> bool:
    f_num = num
    sum_digits: int = 0
    while (num > 0):
        digit: int = int(num % 10)
        sum_digits += int(digit ** 3)
        num = num // 10
    
    return sum_digits == f_num


if __name__ == '__main__':
    num = int(input('Enter number: '))
    print(armstrong_number(num))
