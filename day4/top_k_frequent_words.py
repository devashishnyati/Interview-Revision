"""
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

 

Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.

"""

import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        pq = []
        word_map = {}
        top_k_frequent_words = []
        
        for word in words:
            if word not in word_map:
                word_map[word] = 0
            word_map[word] += 1
        
        for i, word in enumerate(word_map):
            word_node = Node(word, word_map[word])
            if len(pq) < k:
                heapq.heappush(pq, word_node)
            else:
                heapq.heappushpop(pq, word_node)
             
        while pq:
            top_k_frequent_words.append(heapq.heappop(pq).word)
        return top_k_frequent_words[::-1]
        
class Node:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq