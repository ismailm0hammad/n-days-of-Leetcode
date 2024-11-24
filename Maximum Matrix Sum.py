# LeetCode 1975 : Maximum Matrix Sum
# https://leetcode.com/problems/maximum-matrix-sum/description/
class Solution:
  def maxMatrixSum(self, matrix: list[list[int]]) -> int:
    absSum = 0
    minAbs = math.inf
    oddNeg = 0

    for row in matrix:
      for num in row:
        absSum += abs(num)
        minAbs = min(minAbs, abs(num))
        if num < 0:
          oddNeg ^= 1

    return absSum - oddNeg * minAbs * 2