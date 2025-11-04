'''
    Find out that a number is a prime number or not
'''

import math


def prime_number(num: int) -> bool:
    count = 0
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            count += 1
    
    return count > 0


if __name__ == '__main__':
    num = int(input('Enter number: '))
    print(prime_number(num))
