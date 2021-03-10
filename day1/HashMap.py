# Brute Force
# Space is too much. Can be optimized on space
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = [None for _ in range(1000000)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_value = key % 1000000
        self.map[hash_value] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_value = key % 1000000
        if self.map[hash_value] == None:
            return -1
        return self.map[hash_value]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_value = key % 1000000
        self.map[hash_value] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# Double Hashing
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = [[] for _ in range(1001)]
                    
    def __get_hash(self, key):
        hash_value1 = key % 1000
        hash_value2 = key // 1000
        return hash_value1, hash_value2

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_value1, hash_value2 = self.__get_hash(key)
        if len(self.map[hash_value1]) == 0:
            self.map[hash_value1] = [-1 for _ in range(1001)]
        self.map[hash_value1][hash_value2] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_value1, hash_value2 = self.__get_hash(key)
        if len(self.map[hash_value1]) == 0:
            return -1
        return self.map[hash_value1][hash_value2]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_value1, hash_value2 = self.__get_hash(key)
        if len(self.map[hash_value1]) != 0:
            self.map[hash_value1][hash_value2] = -1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


# Chaining
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = [None for _ in range(101)]
        
    def __get_hash(self, key):
        return key%100

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        node = Node(key, value)
        hash_value = self.__get_hash(key)
        if self.map[hash_value] == None:
            self.map[hash_value] = node
        else:
            current = self.map[hash_value]
            while current:
                if current.key == key:
                    current.value = value
                    return 
                elif current.next == None:
                    break
                current = current.next
            current.next = Node(key, value)
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_value = self.__get_hash(key)
        if self.map[hash_value]:
            current = self.map[hash_value]
            while current:
                if current.key == key:
                    return current.value
                current = current.next
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_value = self.__get_hash(key)
        if self.map[hash_value]:
            current = self.map[hash_value]
            prev = self.map[hash_value]
            if not current:
                return
            elif current.key == key:
                self.map[hash_value] = current.next
            else:
                current = current.next
                while current:
                    if current.key == key:
                        prev.next = current.next
                        break
                    else:
                        prev = prev.next
                        current = current.next
            
            
        
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
