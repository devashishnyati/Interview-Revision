class HashMapMethodOne:
    ## Using a straight list of size 10 ^ 6
    ## Very expensive on space as many spaces will be bank
    ## get: O(1)
    ## put: O(1)
    ## delete: O(1)

    def __init__(self):
        self.giant_list = [None for _ in range(1000001)]

    def put(self, key, value):
        self.giant_list[key] = value
      
    def get(self, key):
        return self.giant_list[key] if self.giant_list[key]!= None else -1

    def delete(self, key):
        if self.giant_list[key]:
            self.giant_list[key] = None 

class HashMapMethodTwo:
    ## Using a linked List
    ## 23/36 test cases passed
    ## get: O(n)
    ## put: O(n)
    ## delete: O(n)

    def __init__(self):
        self.giant_list = [None for _ in range(1000)]

    def put(self, key, value):
        node = Node(key, value)
        hash_value = self.__hash(key)
        if not self.giant_list[hash_value]:
            self.giant_list[hash_value] = node
        else:
            curr = self.giant_list[hash_value]
            while curr:
                if curr.key == key:
                    curr.val = value
                    break
                elif curr.next:
                    curr = curr.next
                else:
                    curr.next = node
                    break
                    
      
    def get(self, key):
        hash_value = self.__hash(key)
        if not self.giant_list[hash_value]:
            return -1
        curr = self.giant_list[hash_value]
        while curr:
            if curr.key == key:
                return curr.val
            else:
                curr = curr.next
            
        return -1

    def delete(self, key):
        hash_value = self.__hash(key)
        if self.giant_list[hash_value]:
            curr = self.giant_list[hash_value]
            
            if curr.key == key:
                self.giant_list[hash_value] = curr.next
            else:
                prev = self.giant_list[hash_value]
                curr = curr.next
                while curr:
                    if curr.key == key:
                        prev.next = curr.next
                    else:
                        prev = prev.next
                        curr = curr.next

    def __hash(self, key):
        return key%1000

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class HashMapMethodThree:
    ## Using a binary search tree
    ## 27/36 test cases passed
    ## get: O(logn)
    ## put: O(logn)
    ## delete: O(logn)

    def __init__(self):
        self.giant_list = [None for _ in range(1000)]

    def put(self, key, value):
        tree_node = TreeNode(key, value)
        hash_value = self.__hash(key)
        if not self.giant_list[hash_value]:
            self.giant_list[hash_value] = tree_node

        else:
            curr = self.giant_list[hash_value]
            while curr:
                if curr.key == key:
                    curr.val = value
                    break
                elif key < curr.val:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = tree_node
                        break
                else: 
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = tree_node
                        break
      
    def get(self, key):
        hash_value = self.__hash(key)
        if not self.giant_list[hash_value]:
            return -1
        curr = self.giant_list[hash_value]
        while curr:
            if key == curr.key:
                return curr.val
            elif key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        
        return -1

    def delete(self, key):
        hash_value = self.__hash(key)
        if self.giant_list[hash_value]:
            root = self.giant_list[hash_value]
            self.giant_list[hash_value] = self.__delete_node(root, key)


    def __hash(self, key):
        return key%1000

    def __delete_node(self, root, key):
        if root == None:
            return root
        if key == root.val:
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            
            root.val = self.__find_right_min(root.right)
            root.right = self.__delete_node(root.right, root.val)

        elif key < root.val:
            self.__delete_node(root.left, key)
        
        else:
            self.__delete_node(root.right, key)

    def __find_right_min(self, node):
        while node.left:
            node = node.left
        return node.val



class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None



class HashMapMethodFour:
    ## Double hashing
    ## get: O(1)
    ## put: O(1)
    ## delete: O(1)

    def __init__(self):
        self.giant_list = [None for _ in range(1001)]

    def put(self, key, value):
        hash_one = self.__get_hash_one(key)
        hash_two = self.__get_hash_two(key)
        if not self.giant_list[hash_one]:
            self.giant_list[hash_one] = [None for _ in range(1001)]
        
        self.giant_list[hash_one][hash_two] = value
      
    def get(self, key):
        hash_one = self.__get_hash_one(key)
        hash_two = self.__get_hash_two(key)
        if self.giant_list[hash_one]:
            if self.giant_list[hash_one][hash_two] != None:
                return self.giant_list[hash_one][hash_two]
        return -1

    def delete(self, key):
        hash_one = self.__get_hash_one(key)
        hash_two = self.__get_hash_two(key)
        if self.giant_list[hash_one]:
            if self.giant_list[hash_one][hash_two] != None:
                self.giant_list[hash_one][hash_two] = None
    
    def __get_hash_one(self, key):
        return key % 1001
    
    def __get_hash_two(self, key):
        return key // 1001

if __name__ == "__main__":
    my_map_one = HashMapMethodFour()
    print(my_map_one.put(1,1))
    print(my_map_one.put(2,2))
    print(my_map_one.get(1))
    print(my_map_one.get(3))
    print(my_map_one.put(2,1))
    print(my_map_one.get(2))
    print(my_map_one.delete(2))
    print(my_map_one.get(2))
