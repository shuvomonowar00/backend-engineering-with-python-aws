'''
    Find GCD (Greatest Common Divisor) using linear approach
'''

import math


def find_gcd_linear_approach(num1: int, num2: int) -> int:
    min_num: int = min(num1, num2)
    gcd = 1
    for i in range(1, int(math.sqrt(min_num))+1):
        if num1%i == 0 and num2%i == 0:
            if gcd < i:
                gcd = i
            if num1%(min_num//i) == 0 and num2%(min_num//i) == 0:
                if gcd < (min_num // i):
                    gcd = min_num // i
    return gcd


if __name__ == '__main__':
    num1: int = int(input('Enter num1: '))
    num2: int = int(input('Enter num2: '))
    print(find_gcd_linear_approach(num1 = num1, num2 = num2))


