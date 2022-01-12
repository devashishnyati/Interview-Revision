"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        left, left_wall, right, right_wall = 0, 0, len(height)-1, len(height)-1
        trapped_water = 0
        while left < right:
            # case 1: left is lower than right
            if height[left] < height[right]:
                left += 1
                # case 1.1: if left wall is heigher than left. water is trapped
                if height[left] < height[left_wall]:
                    trapped_water += height[left_wall] - height[left]
                # case 1.2: left wall is lower, no water is trapped. Update left wall
                else:
                    left_wall = left
            # case 2: right is lower than equal to left
            else:
                right -= 1
                # case 2.1: if right wall is heigher than right. water is trapped
                if height[right] < height[right_wall]:
                    trapped_water += height[right_wall] - height[right]
                # case 2.2: left wall is lower, no water is trapped. Update left wall
                else:
                    right_wall = right
        return trapped_water
        