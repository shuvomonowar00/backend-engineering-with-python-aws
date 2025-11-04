'''
    1. Take an input number -> num
    2. While loop with base case -> num > 0
    3. Findout the remainder of the number -> num%10
    4. Append the remainder into the list -> list.append(num%10)
    5. Initialize the the number -> num = num/10
'''

from typing import List


def find_digits(num: int) -> List[int]:
    lst: List[int] = []
    while num > 0:
        lst.append(int(num%10))
        num = num // 10 # To make ensure integer value
    
    # Reverse the digits in the list
    lft_itm = 0
    rht_itm = len(lst)-1
    while lft_itm < rht_itm:
        tmp_itm = lst[lft_itm]
        lst[lft_itm] = lst[rht_itm]
        lst[rht_itm] = tmp_itm
        lft_itm += 1
        rht_itm -= 1
    return lst


if __name__ == '__main__':
    num = int(input('Enter number: '))
    print(find_digits(num))


# Time Complexity -> O(log10(n))