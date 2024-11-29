# LeetCode 2290 : Minimum Obstacle Removal to Reach Corner
# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/description/
class Solution:
  def minimumObstacles(self, grid: list[list[int]]) -> int:
    drctns = ((0, 1), (1, 0), (0, -1), (-1, 0))
    m = len(grid)
    n = len(grid[0])
    minHp = [(grid[0][0], 0, 0)] 
    dstnc = [[math.inf] * n for _ in range(m)]
    dstnc[0][0] = grid[0][0]

    while minHp:
      d, i, j = heapq.heappop(minHp)
      if i == m - 1 and j == n - 1:
        return d
      for dx, dy in drctns:
        x = i + dx
        y = j + dy
        if x < 0 or x == m or y < 0 or y == n:
          continue
        newdstnc = d + grid[i][j]
        if newdstnc < dstnc[x][y]:
          dstnc[x][y] = newdstnc
          heapq.heappush(minHp, (newdstnc, x, y))

    return dstnc[m - 1][n - 1]