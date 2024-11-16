# 3254. Find the Power of K-Size Subarrays I
# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/description/
class Solution:
  def resultsArray(self, nums: list[int], k: int) -> list[int]:
    res = []
    begin = 0

    for i, num in enumerate(nums):
      if i > 0 and num != nums[i - 1] + 1:
        begin = i
      if i >= k - 1:
        res.append(num if i - begin + 1 >= k else -1)

    return res