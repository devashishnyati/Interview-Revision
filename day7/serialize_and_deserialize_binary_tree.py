"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def __init__(self):
        self.DELIMETER = '|'
        self.NONE_STRING = "None"

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
   
        result_string = ""
        if not root:
            return result_string
        
        queue = []
        queue.append(root)
        
       
        
        while queue:
            curr = queue.pop(0)
            if curr:
                result_string += str(curr.val)
                result_string += self.DELIMETER 
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                result_string += self.NONE_STRING
                result_string += self.DELIMETER        
        return result_string[:-1]
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        
        serialized_list = data.split(self.DELIMETER)
        
        root = TreeNode(serialized_list[0])
        
        pointer = 1
        queue = []
        queue.append(root)
        
        while queue:
            curr = queue.pop(0)
            if serialized_list[pointer] == self.NONE_STRING:
                curr.left = None
            else:
                left_node = TreeNode(serialized_list[pointer])
                curr.left = left_node
                queue.append(left_node)
            pointer += 1
            
            if serialized_list[pointer] == self.NONE_STRING:
                curr.right = None
            else:
                right_node = TreeNode(serialized_list[pointer])
                curr.right = right_node
                queue.append(right_node)
            pointer += 1
        
        return root
                
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))