# LeetCode 1574 : Shortest Subarray to be Removed to Make Array Sorted
# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/description/
class Solution:
  def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
    n = len(arr)
    lt = 0
    rt = n - 1

    while lt < n - 1 and arr[lt + 1] >= arr[lt]:
      lt += 1
    while rt > 0 and arr[rt - 1] <= arr[rt]:
      rt -= 1
    res = min(n - 1 - lt, rt)
    i = lt
    j = n - 1
    while i >= 0 and j >= rt and j > i:
      if arr[i] <= arr[j]:
        j -= 1
      else:
        i -= 1
      res = min(res, j - i)

    return res