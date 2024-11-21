# LeetCode 2257 : Count Unguarded Cells in the Grid
# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/description/
class Solution:
  def countUnguarded(
      self,
      m: int,
      n: int,
      guards: list[list[int]],
      walls: list[list[int]],
  ) -> int:
    res = 0
    grid = [[0] * n for _ in range(m)]
    lt = [[0] * n for _ in range(m)]
    rt = [[0] * n for _ in range(m)]
    tp = [[0] * n for _ in range(m)]
    dwn = [[0] * n for _ in range(m)]

    for row, col in guards:
      grid[row][col] = 'G'

    for row, col in walls:
      grid[row][col] = 'W'

    for i in range(m):
      lstCell = 0
      for j in range(n):
        if grid[i][j] == 'G' or grid[i][j] == 'W':
          lstCell = grid[i][j]
        else:
          lt[i][j] = lstCell
      lstCell = 0
      for j in range(n - 1, -1, -1):
        if grid[i][j] == 'G' or grid[i][j] == 'W':
          lstCell = grid[i][j]
        else:
          rt[i][j] = lstCell

    for j in range(n):
      lstCell = 0
      for i in range(m):
        if grid[i][j] == 'G' or grid[i][j] == 'W':
          lstCell = grid[i][j]
        else:
          tp[i][j] = lstCell
      lstCell = 0
      for i in range(m - 1, -1, -1):
        if grid[i][j] == 'G' or grid[i][j] == 'W':
          lstCell = grid[i][j]
        else:
          dwn[i][j] = lstCell

    for i in range(m):
      for j in range(n):
        if (grid[i][j] == 0 and lt[i][j] != 'G' and rt[i][j] != 'G' and
                tp[i][j] != 'G' and dwn[i][j] != 'G'):
          res += 1

    return res