# LeetCode 1331 : Rank Transform of an Array
# https://leetcode.com/problems/rank-transform-of-an-array/description/
class Solution:
  def arrayRankTransform(self, arr: list[int]) -> list[int]:
    rank = {}

    for a in sorted(arr):
      if a not in rank:
        rank[a] = len(rank) + 1

    return map(rank.get, arr)