"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = [1 for _ in range(len(nums))]
        right_product = [1 for _ in range(len(nums))]
        
        for i in range(1, len(nums)):
            left_product[i] = left_product[i-1] * nums[i-1]
            
        # print(left_product)
        
        for j in range(len(nums)-2, -1, -1):
            right_product[j] = right_product[j+1] * nums[j+1]
            
        # print(right_product)
        
        for i in range(len(left_product)):
            left_product[i] = left_product[i] * right_product[i]
            
        return left_product