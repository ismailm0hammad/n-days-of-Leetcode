# LeetCode 2461 : Maximum Sum of Distinct Subarrays With Length K
# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/
class Solution:
  def maximumSubarraySum(self, nums: list[int], k: int) -> int:
    res = 0
    sub_sum = 0
    unq = 0
    count = collections.Counter()

    for i, num in enumerate(nums):
      sub_sum += num
      count[num] += 1
      if count[num] == 1:
        unq += 1
      if i >= k:
        count[nums[i - k]] -= 1
        if count[nums[i - k]] == 0:
          unq -= 1
        sub_sum -= nums[i - k]
      if i >= k - 1 and unq == k:
        res = max(res, sub_sum)

    return res