# LeetCode 2530 : Maximal Score After Applying K Operations
# https://leetcode.com/problems/maximal-score-after-applying-k-operations/description/
class Solution:
  def maxKelements(self, nums: list[int], k: int) -> int:
    ans = 0
    maxHeap = [-num for num in nums]
    heapq.heapify(maxHeap)

    for _ in range(k):
      num = -heapq.heappop(maxHeap)
      ans += num
      heapq.heappush(maxHeap, -math.ceil(num / 3))

    return ans