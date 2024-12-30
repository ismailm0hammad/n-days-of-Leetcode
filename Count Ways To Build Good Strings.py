# LeetCode 2466 : Count Ways To Build Good Strings
# https://leetcode.com/problems/count-ways-to-build-good-strings/description/
class Solution:
  def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
    kMod = 1_000_000_007
    res = 0
    dp = [1] + [0] * high

    for i in range(1, high + 1):
      if i >= zero:
        dp[i] = (dp[i] + dp[i - zero]) % kMod
      if i >= one:
        dp[i] = (dp[i] + dp[i - one]) % kMod
      if i >= low:
        res = (res + dp[i]) % kMod

    return res