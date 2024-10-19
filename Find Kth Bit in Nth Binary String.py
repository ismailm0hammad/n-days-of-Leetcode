# LeetCode 1545 : Find Kth Bit in Nth Binary String
# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description/
class Solution:
  def findKthBit(self, n: int, k: int) -> str:
    if n == 1:
      return '0'
    midIndex = pow(2, n - 1)  # 1-indexed
    if k == midIndex:
      return '1'
    if k < midIndex:
      return self.findKthBit(n - 1, k)
    return '1' if self.findKthBit(n - 1, midIndex * 2 - k) == '0' else '0'