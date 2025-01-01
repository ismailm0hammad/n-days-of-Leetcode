# LeetCode 1422 : Maximum Score After Splitting a String
# https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/
class Solution:
  def maxScore(self, s: str) -> int:
    res = 0
    z0s = 0
    o1s = s.count('1')

    for i in range(len(s) - 1):
      if s[i] == '0':
        z0s += 1
      else:
        o1s -= 1
      res = max(res, z0s + o1s)

    return res