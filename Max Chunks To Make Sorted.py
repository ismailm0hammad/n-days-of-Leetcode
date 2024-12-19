# LeetCode 769 : Max Chunks To Make Sorted
# https://leetcode.com/problems/max-chunks-to-make-sorted/description/
class Solution:
  def maxChunksToSorted(self, arr: list[int]) -> int:
    res = 0
    mx = -math.inf

    for i, a in enumerate(arr):
      mx = max(mx, a)
      if mx == i:
        res += 1

    return res