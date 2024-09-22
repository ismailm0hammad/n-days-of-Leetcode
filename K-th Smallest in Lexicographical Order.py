# LeetCode 440 : K-th Smallest in Lexicographical Order
# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/description/
class Solution:
  def findKthNumber(self, n: int, k: int) -> int:
    riz = 1
    i = 1
    while i < k:
      gap = self.help_getGap(riz, riz + 1, n)
      if i + gap <= k:
        i += gap
        riz += 1
      else:
        i += 1
        riz *= 10

    return riz

  def help_getGap(self, a, b, n):
    gap = 0
    while a <= n:
      gap += min(n + 1, b) - a
      a *= 10
      b *= 10
    return gap