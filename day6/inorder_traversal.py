class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def inorder_recursive(self, root):
        # base condition
        if not root:
            return None

        # logic and recursion
        self.inorder_recursive(root.left)
        print(root.val)
        self.inorder_recursive(root.right)

    def inorder_iterative(self, root):
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            print(node.val)
            root = root.right
        


nodes = [5, 3, 7, 1, 4, 6, None]
d = {}
 
    # create `n` new tree nodes, each having a value from 0 to `n-1`,
    # and store them in a dictionary
for i in range(len(nodes)):
    d[i] = TreeNode(i)

node_5 = TreeNode(5)
node_3 = TreeNode(3)
node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_7 = TreeNode(7)
node_4 = TreeNode(4)
node_6 = TreeNode(6)


node_1.left = node_3
node_1.right = node_7
node_3.left = 