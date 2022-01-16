"""
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
"""

class SolutionOne:
    def subarraySum(self, nums: List[int], k: int) -> int:
        output = 0
        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                if curr_sum == k:
                    output += 1
                    
        return output
                

class SolutionTwo:
    def subarraySum(self, nums: List[int], k: int) -> int:
        output, curr_sum = 0, 0
        sum_map = {0:1}
    
        for i in range(len(nums)):
            curr_sum += nums[i]
            # if we have seen curr_sum - k that means the sum of nums from the index where we added curr_sum in map to current index is k
            if curr_sum - k in sum_map:
                output += sum_map[curr_sum - k]
            if curr_sum not in sum_map:
                sum_map[curr_sum] = 0
                # add curr_sum in the map for future retrieval
            sum_map[curr_sum] += 1
        return output
                