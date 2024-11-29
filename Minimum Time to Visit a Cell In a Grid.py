# LeetCode 2577 : Minimum Time to Visit a Cell In a Grid
# https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/description/
class Solution:
  def minimumTime(self, grid: list[list[int]]) -> int:
    if grid[0][1] > 1 and grid[1][0] > 1:
      return -1

    drcxns = ((0, 1), (1, 0), (0, -1), (-1, 0))
    m = len(grid)
    n = len(grid[0])
    minHp = [(0, 0, 0)] 
    seen = {(0, 0)}

    while minHp:
      time, i, j = heapq.heappop(minHp)
      if i == m - 1 and j == n - 1:
        return time
      for dx, dy in drcxns:
        x = i + dx
        y = j + dy
        if x < 0 or x == m or y < 0 or y == n:
          continue
        if (x, y) in seen:
          continue
        xtraWait = 1 if (grid[x][y] - time) % 2 == 0 else 0
        nextTime = max(time + 1, grid[x][y] + xtraWait)
        heapq.heappush(minHp, (nextTime, x, y))
        seen.add((x, y))