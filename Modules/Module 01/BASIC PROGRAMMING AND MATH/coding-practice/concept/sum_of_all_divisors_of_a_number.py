'''
    Find the sum of all divisors of a number
'''

import math


def sum_divisors(num: int) -> int:
    sum_div: int = 0
    for i in range(1, int(math.sqrt(num))+1):
        if num % i == 0:
            sum_div += i
            if i != num // i:
                sum_div += num // i
                
    return sum_div



if __name__ == '__main__':
    num: int = int(input('Enter the number: '))
    print(sum_divisors(num))