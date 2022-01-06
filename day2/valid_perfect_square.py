"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false
"""


class PerfectSquare:
    def is_valid_perfect_square(self, num):
        for i in range(num+1):
            if i*i == num:
                return True
        return False

class PerfectSquareBS:
    def is_valid_perfect_square(self, num):
        if num == 1:
            return True
        low = 1
        high = num // 2
        while low <= high:
            mid = low + (high-low)//2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                high = mid - 1
            else:
                low = mid + 1
        return False

if __name__ == "__main__":
    ps = PerfectSquareBS()
    print(ps.is_valid_perfect_square(4))
    print(ps.is_valid_perfect_square(1))
    print(ps.is_valid_perfect_square(10))
