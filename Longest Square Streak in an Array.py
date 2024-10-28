# LeetCode 2501 : Longest Square Streak in an Array
# https://leetcode.com/problems/longest-square-streak-in-an-array/description/
class Solution:
    def longestSquareStreak(self, nums):
        nums = sorted(set(nums), reverse=True)
        max_num = max(nums)
        dp = {}
        for num in nums:
            dp[num] = 1 
            squared_num = num * num
            
            if squared_num <= max_num and squared_num in dp:
                dp[num] += dp[squared_num]
        
        riz = max(dp.values(), default=0)
        return riz if riz >= 2 else -1