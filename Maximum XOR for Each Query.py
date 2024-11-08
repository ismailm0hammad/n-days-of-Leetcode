# LeetCode 1829 : Maximum XOR for Each Query
# https://leetcode.com/problems/maximum-xor-for-each-query/description/
class Solution:
  def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
    mx = (1 << maximumBit) - 1
    res = []
    xors = 0

    for num in nums:
      xors ^= num
      res.append(xors ^ mx)

    return res[::-1]