# LeetCode 2938 : Separate Black and White Balls
# https://leetcode.com/problems/separate-black-and-white-balls/description/
class Solution:
  def minimumSteps(self, s: str) -> int:
    ans = 0
    ones = 0

    for c in s:
      if c == '1':
        ones += 1
      else: 
        ans += ones

    return ans