# LeetCode 2940 : Find Building Where Alice and Bob Can Meet
# https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/description/
from dataclasses import dataclass

@dataclass
class IndexedQuery:
  qryIndx: int
  a: int
  b: int
  def __iter__(self):
    yield self.qryIndx
    yield self.a
    yield self.b

class Solution:
  def leftmostBuildingQueries(self, heights: list[int], queries: list[list[int]]) -> list[int]:
    res = [-1] * len(queries)
    stack = []
    hgtIndx = len(heights) - 1
    for qryIndx, a, b in sorted([IndexedQuery(i, min(a, b), max(a, b)) for i, (a, b) in enumerate(queries)], key=lambda x: -x.b):
      if a == b or heights[a] < heights[b]: res[qryIndx] = b
      else:
        while hgtIndx > b:
          while stack and heights[stack[-1]] <= heights[hgtIndx]: stack.pop()
          stack.append(hgtIndx)
          hgtIndx -= 1
        j = self.helpLastGreater(stack, a, heights)
        if j != -1: res[qryIndx] = stack[j]
    return res

  def helpLastGreater(self, A: list[int], target: int, heights: list[int]) -> int:
    l, r = -1, len(A) - 1
    while l < r:
      m = (l + r + 1) // 2
      if heights[A[m]] > heights[target]: l = m
      else: r = m - 1
    return l