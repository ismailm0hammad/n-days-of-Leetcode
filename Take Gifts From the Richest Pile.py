# LeetCode 2558 : Take Gifts From the Richest Pile
# https://leetcode.com/problems/take-gifts-from-the-richest-pile/description/
class Solution:
  def pickGifts(self, gifts: list[int], k: int) -> int:
    maxHp = [-gift for gift in gifts]
    heapq.heapify(maxHp)

    for _ in range(k):
      squaredMax = math.isqrt(-heapq.heappop(maxHp))
      heapq.heappush(maxHp, -squaredMax)

    return -sum(maxHp)