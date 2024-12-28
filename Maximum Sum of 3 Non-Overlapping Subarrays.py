# LeetCode 689 : Maximum Sum of 3 Non-Overlapping Subarrays
# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/description/
class Solution:
  def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
    n = len(nums) - k + 1
    sums = [0] * n
    l = [0] * n
    r = [0] * n

    subSum = 0
    for i, num in enumerate(nums):
      subSum += num
      if i >= k:
        subSum -= nums[i - k]
      if i >= k - 1:
        sums[i - k + 1] = subSum

    maxIdx = 0
    for i in range(n):
      if sums[i] > sums[maxIdx]:
        maxIdx = i
      l[i] = maxIdx

    maxIdx = n - 1
    for i in range(n - 1, -1, -1):
      if sums[i] >= sums[maxIdx]:
        maxIdx = i
      r[i] = maxIdx

    res = [-1, -1, -1]

    for i in range(k, n - k):
      if (res[0] == -1 or
          sums[res[0]] + sums[res[1]] + sums[res[2]] <
              sums[l[i - k]] + sums[i] + sums[r[i + k]]):
        res[0] = l[i - k]
        res[1] = i
        res[2] = r[i + k]

    return res