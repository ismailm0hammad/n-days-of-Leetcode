# LeetCode 2064 : Minimized Maximum of Products Distributed to Any Store
# https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/description/
class Solution:
  def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
    lt = 1
    rt = max(quantities)

    def numStores(md):
      return sum((q - 1) // md + 1 for q in quantities)

    while lt < rt:
      md = (lt + rt) // 2
      if numStores(md) <= n:
        rt = md
      else:
        lt = md + 1

    return lt