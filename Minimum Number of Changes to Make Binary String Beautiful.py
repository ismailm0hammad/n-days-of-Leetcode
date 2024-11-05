# LeetCode 2914 : Minimum Number of Changes to Make Binary String Beautiful
# https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/description/
class Solution:
  def minChanges(self, s: str) -> int:
    return sum(a != b for a, b in zip(s[::2], s[1::2]))