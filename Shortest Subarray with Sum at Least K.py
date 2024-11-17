# LeetCode 862 : Shortest Subarray with Sum at Least K
# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/
class Solution:
  def shortestSubarray(self, nums: list[int], k: int) -> int:
    n = len(nums)
    res = n + 1
    dq = collections.deque()
    prfx = list(itertools.accumulate(nums, initial=0))

    for i in range(n + 1):
      while dq and prfx[i] - prfx[dq[0]] >= k:
        res = min(res, i - dq.popleft())
      while dq and prfx[i] <= prfx[dq[-1]]:
        dq.pop()
      dq.append(i)

    return res if res <= n else -1