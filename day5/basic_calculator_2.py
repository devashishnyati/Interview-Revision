"""
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5

"""

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = []
        i = 0
        operator = '+'
        num = 0
        for i in range(len(s)):
            char = s[i]
            
            if char.isdigit():
                num = num * 10 + int(char)
            if not char.isdigit() or i == len(s)-1:
                if operator == '+':
                    stack.append(num)
                if operator == '-':
                    stack.append(-num)
                if operator == '*':
                    stack.append(stack.pop()*num)
                if operator == '/':
                    stack.append(int(stack.pop()/num))
                operator = char
                num = 0
                    
        result = 0
        while stack:
            result += stack.pop()
        return result