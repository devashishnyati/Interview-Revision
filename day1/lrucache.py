"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
"""

class Node:
    def __init__(self):
        self.key = 0
        self.val = 0
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cache_map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.capacity = capacity

    def __add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def __remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None

    def __remove_from_tail(self):
        remove_node = self.tail.prev
        self.__remove_node(remove_node)
        return remove_node.key

    def get(self, key):
        if key not in self.cache_map:
            return -1
        node = self.cache_map[key]
        self.__remove_node(node)
        self.__add_to_head(node)
        return node.val

    def put(self, key, value):
        if key in self.cache_map:
            node = self.cache_map[key]
            node.val = value
            self.__remove_node(node)
            self.__add_to_head(node)
        else:
            node = Node()
            node.val = value
            node.key = key
            self.cache_map[key] = node
            self.__add_to_head(node)
            self.size += 1
            if self.size > self.capacity:
                remove_node_key = self.__remove_from_tail()
                del self.cache_map[remove_node_key]
                self.size -=1


if __name__ == "__main__":
    lru_cache = LRUCache(2)
    print(lru_cache.get(1))
    lru_cache.put(1,1)
    lru_cache.put(2,2)
    print(lru_cache.get(1))
    lru_cache.put(3,3)
    print(lru_cache.get(2))
    lru_cache.put(4,4)
    print(lru_cache.get(1))
    print(lru_cache.get(3))
    print(lru_cache.get(4))


