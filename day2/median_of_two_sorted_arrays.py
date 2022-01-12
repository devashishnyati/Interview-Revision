"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 


"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        len_nums1, len_nums2 = len(nums1), len(nums2)
        
        left_size = (len_nums1 + len_nums2 + 1) // 2
        start = 0
        end = len_nums1
        is_even = ((len_nums1 + len_nums2) % 2) == 0
        while start <= end:
            a_part = (start + end) // 2
            b_part = left_size - a_part
            print(a_part, b_part)
            aleftmax = nums1[a_part - 1] if a_part > 0 else float("-inf") 
            arightmin = nums1[a_part] if a_part < len_nums1 else float("inf") 
            bleftmax = nums2[b_part - 1] if b_part > 0 else float("-inf") 
            brightmin = nums2[b_part] if b_part < len_nums2 else float("inf") 
            
            if aleftmax <= brightmin and bleftmax <= arightmin:
                if not is_even:
                    return max(aleftmax, bleftmax)
                else:
                    return (max(aleftmax, bleftmax) + min(arightmin, brightmin))/ 2
            elif aleftmax > brightmin:
                end = a_part - 1
            elif bleftmax > arightmin:
                start = a_part + 1
            
