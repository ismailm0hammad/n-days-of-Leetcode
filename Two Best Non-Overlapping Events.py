# LeetCode 2054 : Two Best Non-Overlapping Events
# https://leetcode.com/problems/two-best-non-overlapping-events/description/
class Solution:
  def maxTwoEvents(self, events: list[list[int]]) -> int:
    res = 0
    maxVal = 0
    evnts = [] 

    for s, e, v in events:
      evnts.append((s, 1, v))
      evnts.append((e + 1, 0, v))

    evnts.sort()

    for _, isStart, value in evnts:
      if isStart:
        res = max(res, value + maxVal)
      else:
        maxVal = max(maxVal, value)

    return res