class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        t_map = {}
        for char in t:
            if char not in t_map:
                t_map[char] = 0
            t_map[char] += 1 
        final_map = t_map.copy()
        # print(final_map)
        minimum_substring = s
        found = False
        for i in range(len(s)):
            current_substring = ''
            for j in range(i, len(s)):
                
                current_substring += s[j]
                
                if s[j] in t_map and t_map[s[j]] != 0:
                    t_map[s[j]] -= 1

                if sum(t_map.values()) == 0:
                    found = True
                    if len(current_substring) < len(minimum_substring):
                        minimum_substring = current_substring
                        t_map = final_map.copy()
                    break
            t_map = final_map.copy()
                 
        if found:
            return minimum_substring
        else:
            return ""