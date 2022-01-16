"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map_s, char_map_t = {}, {}
        for i in range(len(s)):
            if s[i] not in char_map_s:
                char_map_s[s[i]] = t[i]
            else:
                if char_map_s[s[i]] != t[i]:
                    return False
            if t[i] not in char_map_t:
                char_map_t[t[i]] = s[i]
            else:
                if char_map_t[t[i]] != s[i]:
                    return False
        return True