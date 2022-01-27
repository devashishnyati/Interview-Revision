"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_common = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < len(longest_common) and j < len(strs[i]):
                if longest_common[j] == strs[i][j]:
                    j += 1
                else:
                    break
            longest_common = longest_common[:j]
        return longest_common