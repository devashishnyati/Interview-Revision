"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""

class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        stack = []
        for char in s:
            if char not in parentheses_map:
                stack.append(char)
            else:
                # ']' case
                if len(stack) == 0:
                    return False
                elif stack.pop() != parentheses_map[char]:
                    return False
        # '[' case 
        if len(stack) != 0:
            return False
        return True