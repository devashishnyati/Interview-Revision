"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1

"""

# nums = [4,5,6,7,0,1,2]
left = 4
right = 4
mid = 4


class Searching:
    def search(self, nums: List[int], target: int) -> int: 
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

class SearchingRecursively:
    def search(self, nums: List[int], target: int) -> int:
        return self.__helper(nums, target, 0, len(nums)-1)

    def __helper(self, nums, target, low, high):
        # base condition
        if low > high:
            return -1
        
        # logic
        mid = low + (high-low)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] <= nums[high]:
            if nums[mid] < target <= nums[high]:
                return self.__helper(nums, target, mid+1, high)
            else:
                return self.__helper(nums, target, low, mid-1)
        else:
            if nums[low] <= target < nums[mid]:
                return self.__helper(nums, target, low, mid-1)
            else:
                return self.__helper(nums, target, mid+1, high)
