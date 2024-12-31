# LeetCode 983 : Minimum Cost For Tickets
# https://leetcode.com/problems/minimum-cost-for-tickets/description/
class Solution:
  def mincostTickets(self, days: list[int], costs: list[int]) -> int:
    res = 0
    last7 = collections.deque()
    last30 = collections.deque()

    for day in days:
      while last7 and last7[0][0] + 7 <= day:
        last7.popleft()
      while last30 and last30[0][0] + 30 <= day:
        last30.popleft()
      last7.append([day, res + costs[1]])
      last30.append([day, res + costs[2]])
      res = min(res + costs[0], last7[0][1], last30[0][1])

    return res