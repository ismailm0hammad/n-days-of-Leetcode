# LeetCode 2924 : Find Champion II
# https://leetcode.com/problems/find-champion-ii/description/
class Solution:
  def findChampion(self, n: int, edges: list[list[int]]) -> int:
    inDgrs = [0] * n

    for _, v in edges:
      inDgrs[v] += 1

    return (-1 if inDgrs.count(0) > 1 else inDgrs.index(0))