"""
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = set()
        slow, fast = 0, 0
        max_string_len = 0
        cur_max_len = 0
        while fast < len(s):
            if s[fast] not in lookup:
                cur_max_len += 1
                max_string_len = max(max_string_len, cur_max_len)
                lookup.add(s[fast])
                fast += 1
            else:
                lookup.remove(s[slow])
                slow += 1
                cur_max_len -= 1
        return max_string_len
                
class SolutionTwo:
    # O(n^2)
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = set()
        max_str_len = 0
        curr_str_len = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] not in lookup:
                    curr_str_len += 1
                    lookup.add(s[j])
                    max_str_len = max(max_str_len, curr_str_len)
                else:
                    lookup = set()
                    curr_str_len = 0
                
                    break
            
        return max_str_len
