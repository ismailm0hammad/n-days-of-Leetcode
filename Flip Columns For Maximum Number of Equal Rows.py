# LeetCode 1072 : Flip Columns For Maximum Number of Equal Rows
# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/description/
class Solution:
  def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
    ptrns = [tuple(a ^ row[0] for a in row) for row in matrix]
    return max(Counter(ptrns).values())