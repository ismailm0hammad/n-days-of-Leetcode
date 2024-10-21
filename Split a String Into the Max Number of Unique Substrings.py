# LeetCode 1593 : Split a String Into the Max Number of Unique Substrings
# https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/description/

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.riz = 0
        self.dfs(s, 0, set())
        return self.riz
    
    def dfs(self, s: str, start: int, seen: set) -> None:
        if start == len(s):
            self.riz = max(self.riz, len(seen))
            return
        
        for i in range(start + 1, len(s) + 1):
            cand = s[start:i]
            if cand in seen:
                continue
            seen.add(cand)
            self.dfs(s, i, seen)
            seen.remove(cand)