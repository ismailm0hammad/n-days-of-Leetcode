# LeetCode 2554 : Maximum Number of Integers to Choose From a Range I
# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/description/
class Solution:
  def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
    res = 0
    curSum = 0
    bannedSet = set(banned)

    for i in range(1, n + 1):
      if i not in bannedSet and curSum + i <= maxSum:
        res += 1
        curSum += i

    return res