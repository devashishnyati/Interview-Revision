"""
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
"""

class PeakElement:
   def find_peak_element(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if self.__get_value(nums, mid-1) < self.__get_value(nums, mid) > self.__get_value(nums, mid+1):
                return mid
            elif self.__get_value(nums, mid-1) < self.__get_value(nums, mid) < self.__get_value(nums, mid+1):
                left = mid+1
            else:
                right = mid-1
            
    def __get_value(self, nums, indx):
        if indx == -1 or indx == len(nums):
            return float('-inf')
        return nums[indx]