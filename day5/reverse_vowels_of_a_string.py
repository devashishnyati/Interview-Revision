"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
"""
from collections import deque
class SolutionOne:
    def reverseVowels(self, s: str) -> str:
        q = deque([])
        vowel = set(['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U'])
        for i, char in enumerate(s):
            if char in vowel:
                q.append(char)
                
        i = 0
        ret_str = ''
        while i < len(s):
            if s[i] in vowel:
                vowel_node = q.pop()
                ret_str += vowel_node
            else:
                ret_str += s[i]
            i += 1
        
        return ret_str

        
class SolutionTwo:
    def reverseVowels(self, s: str) -> str:
        vowel = set(['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U'])
        left = 0
        right = len(s)-1
        char_list = [char for char in s]
        while left < right:
            while char_list[left] not in vowel and left < right:
                left += 1
            while char_list[right] not in vowel and left < right:
                right -= 1
            char_list[left], char_list[right] = char_list[right], char_list[left]
            left += 1
            right -= 1
        return ''.join(char_list)