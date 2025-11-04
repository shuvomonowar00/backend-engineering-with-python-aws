'''
    1. Take a input number
    2. Extract digits from the number
    3. Multiply each digit with 10 ** digit where initially digit = log10(num)
       and each iteration digit = digit-1
    4. Make sum of the all multiplies new numbers
'''

import math

# Method - 01
# def reverse_number(num: int) -> int:
#     sum_digits: int = 0

#     # Find the length of the number and make sure to decrease 1
#     num_len: int = int(math.log10(num))

#     # Extract the digits
#     while num > 0:
#         digit: int = int(num % 10)
#         sum_digits += (digit * (10 ** num_len)) # Multiply the extracted digit with 10 ** num_len and sum them with sum_digits
#         num_len -= 1
#         num = num // 10
    
#     return sum_digits


# Method - 02
# def reverse_number(num: int) -> int:
#     sum_digits: int = 0

#     # Extract the digits
#     while num > 0:
#         digit: int = int(num % 10)
#         sum_digits = (sum_digits*10)+digit
#         num = num // 10
    
#     return sum_digits


# Method - 03 (For negetive number)
def reverse_number(num: int) -> int:
    sum_digits: int = 0

    while num != 0:
        digit: int = int(math.fmod(num, 10))
        sum_digits = (sum_digits*10)+digit
        num = num // 10
    
    return sum_digits


if __name__ == '__main__':
    num: int = int(input('Enter number: '))
    print(reverse_number(num))