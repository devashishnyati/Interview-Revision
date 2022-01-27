"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # left, root, right -> inorder
        return self.__helper(root)
    
    def __helper(self, node):
        stack = []
        prev = float('-inf')
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            current = stack.pop()
            if current.val <= prev:
                return False
            prev = current.val
            node = current.right
        return True
        
       