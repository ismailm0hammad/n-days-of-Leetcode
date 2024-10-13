# LeetCode 2406 : Divide Intervals Into Minimum Number of Groups
# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/description/
class Solution:
  def minGroups(self, intervals: list[list[int]]) -> int:
    minHeap = []  
    for left, right in sorted(intervals):
      if minHeap and left > minHeap[0]:
        heapq.heappop(minHeap)
      heapq.heappush(minHeap, right)

    return len(minHeap)