"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count_map = {}
        pq = []
        result_list = []
        for num in nums:
            if num not in num_count_map:
                num_count_map[num] = 0
            num_count_map[num] += 1
            
        for num in num_count_map:
            num_node = Node(num, num_count_map[num])
            if len(pq) == k:
                heapq.heappushpop(pq, num_node)
            else:
                heapq.heappush(pq, num_node)
        while pq:
            result_list.append(heapq.heappop(pq).num)
        return result_list
    
class Node:
    def __init__(self, num, freq):
        self.num = num
        self.freq = freq
        
    def __lt__(self, other):
        return self.freq < other.freq
        
