"""
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

 

Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
"""
import random

class RandomizedSet:
    def __init__(self):
        self.value_map = {}
        self.random_list = []
        self.index_pointer = 0

    def insert(self, val):
        if val in self.value_map:
            return False
        self.random_list.append(val)
        self.value_map[val] = self.index_pointer
        self.index_pointer += 1
        return True

    def remove(self, val):
        if val not in  self.value_map:
            return False
        value_index = self.value_map[val]
        self.random_list[value_index] = self.random_list[-1]
        self.value_map[self.random_list[value_index]] = value_index
        self.index_pointer -= 1
        self.random_list.pop()
        self.value_map.pop(val)
        return True

    def get_random(self):
        # print(self.random_list)
        return random.choice(self.random_list)


if __name__ == "__main__":
    random_set = RandomizedSet()
    print(random_set.remove(2))
    print(random_set.insert(1))
    print(random_set.insert(2))
    print(random_set.insert(2))
    print(random_set.insert(3))
    print(random_set.insert(4))
    print(random_set.get_random())
    print(random_set.remove(2))
    print(random_set.get_random())