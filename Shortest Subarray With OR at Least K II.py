# LeetCode 3097 : Shortest Subarray With OR at Least K II
# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/description/
class Solution:
  def minimumSubarrayLength(self, nums: list[int], k : int) -> int:
    riz = len(nums) + 1
    ors = 0
    cnt = collections.Counter()

    l = 0
    for r, num in enumerate(nums):
      ors = self._orNum(ors, num, cnt)
      while ors >= k and l <= r:
        riz = min(riz, r - l + 1)
        ors = self._undoOrNum(ors, nums[l], cnt)
        l += 1

    return -1 if riz == len(nums) + 1 else riz

  def _orNum(self, ors, num, cnt):
    for i in range(30):
      if num >> i & 1:
        cnt[i] += 1
        if cnt[i] == 1:
          ors += 1 << i
    return ors

  def _undoOrNum(self, ors, num, cnt):
    for i in range(30):
      if num >> i & 1:
        cnt[i] -= 1
        if cnt[i] == 0:
          ors -= 1 << i
    return ors