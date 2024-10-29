# LeetCode 2684 : Maximum Number of Moves in a Grid
# https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/description/
class Solution:
  def maxMoves(self, grid: list[list[int]]) -> int:
    rws = len(grid)
    clns = len(grid[0])
    dp = [[0] * clns for _ in range(rws)]

    for j in range(clns - 2, -1, -1):
      for i in range(rws):
        if grid[i][j + 1] > grid[i][j]:
          dp[i][j] = 1 + dp[i][j + 1]
        if i > 0 and grid[i - 1][j + 1] > grid[i][j]:
          dp[i][j] = max(dp[i][j], 1 + dp[i - 1][j + 1])
        if i + 1 < rws and grid[i + 1][j + 1] > grid[i][j]:
          dp[i][j] = max(dp[i][j], 1 + dp[i + 1][j + 1])

    return max(dp[i][0] for i in range(rws))