# LeetCode 2275 : Largest Combination With Bitwise AND Greater Than Zero
# https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/description/
class Solution:
    def largestCombination(self, candidates: list[int]) -> int:
        max_combination = 0
        for i in range(24):
            count = 0
            for c in candidates:
                if (c >> i) & 1:
                    count += 1
            max_combination = max(max_combination, count)
        return max_combination