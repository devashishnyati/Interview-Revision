"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
"""

class SolutionOne:
    def maxSubArray(self, nums: List[int]) -> int:     
        output = float('-inf')
        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                output = max(output, curr_sum)
                
        return output
        
class SolutionTwo:
    def maxSubArray(self, nums: List[int]) -> int:     
        dp = [float('-inf')]
        for i in range(len(nums)):
            dp.append(max((dp[i]+nums[i]), nums[i]))
        return max(dp)