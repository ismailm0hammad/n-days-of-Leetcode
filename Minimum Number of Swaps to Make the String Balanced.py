# LeetCode 1963 : Minimum Number of Swaps to Make the String Balanced
# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/
class Solution:
  def minSwaps(self, s: str) -> int:
    unmatched = 0
    for c in s:
      if c == '[':
        unmatched += 1
      elif unmatched > 0:
        unmatched -= 1

    return (unmatched + 1) // 2