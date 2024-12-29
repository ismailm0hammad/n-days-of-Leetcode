# LeetCode 1639 : Number of Ways to Form a Target String Given a Dictionary
# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/description/
class Solution:
  def numWays(self, words: list[str], target: str) -> int:
    kMod = 1_000_000_007
    dp = [0] * (len(target) + 1)
    dp[0] = 1

    for j in range(len(words[0])):
      count = collections.Counter(word[j] for word in words)
      for i in range(len(target), 0, -1):
        dp[i] += dp[i - 1] * count[target[i - 1]]
        dp[i] %= kMod

    return dp[len(target)]