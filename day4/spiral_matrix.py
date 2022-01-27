"""
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        left, right, top, bottom = 0, len(matrix[0]), 0, len(matrix)
        while left < right and top < bottom:

            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1
            for i in range(top, bottom):
                result.append(matrix[i][right-1])
            right -= 1
            if top < bottom:
                for i in range(right-1, left-1, -1):
                    result.append(matrix[bottom-1][i])
                bottom -= 1
            if left < right:
                for i in range(bottom-1, top-1, -1):
                    result.append(matrix[i][left])
                left += 1
        return result