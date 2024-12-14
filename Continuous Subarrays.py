# LeetCode 2762 : Continuous Subarrays
# https://leetcode.com/problems/continuous-subarrays/description/
class Solution:
  def continuousSubarrays(self, nums: list[int]) -> int:
    res = 1
    lt = nums[0] - 2
    rt = nums[0] + 2
    l = 0

    for r in range(1, len(nums)):
      if lt <= nums[r] <= rt:
        lt = max(lt, nums[r] - 2)
        rt = min(rt, nums[r] + 2)
      else:
        lt = nums[r] - 2
        rt = nums[r] + 2
        l = r
        while nums[r] - 2 <= nums[l] <= nums[r] + 2:
          lt = max(lt, nums[l] - 2)
          rt = min(rt, nums[l] + 2)
          l -= 1
        l += 1
      res += r - l + 1

    return res
