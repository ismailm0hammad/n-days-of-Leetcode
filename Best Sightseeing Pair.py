# leetCode 1014 : Best Sightseeing Pair
# https://leetcode.com/problems/best-sightseeing-pair/description/
class Solution:
  def maxScoreSightseeingPair(self, values: list[int]) -> int:
    res = 0
    bestPrev = 0

    for value in values:
      res = max(res, value + bestPrev)
      bestPrev = max(bestPrev, value) - 1

    return res