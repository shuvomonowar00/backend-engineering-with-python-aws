'''
    Finding GCD (Greatest Common Devisor) usng Eucledian algorithm

    Algorithm and pseudocode
    ------------------------
    1. num1, num2
    2. while min(num1, num2) > 0
    3. if num1 > num2 -> num1 %= num2, else num2 %= num1
    4. return max(num1, num2) -> After completion the loop 
'''
from typing import List


class Solution_01:
    # def findGCD(self, nums: List[int]) -> int:
    #     x = min(nums)
    #     y = max(nums)
    #     while x > 0 and y > 0:
    #         if x > y:
    #             x = x%y
    #         else:
    #             y = y%x
            
    #     return max(x,y)

    def findGCD(self, nums: List[int]) -> int:
        x = min(nums)
        y = max(nums)
        while min(x, y) > 0:
            if x > y:
                x %= y
            else:
                y %= x
            
        return max(x,y)


if __name__ == '__main__':
    obj = Solution_01()
    print(obj.findGCD([3,3]))
