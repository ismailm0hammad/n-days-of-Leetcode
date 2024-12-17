# LeetCode 2182 : Construct String With Repeat Limit
# https://leetcode.com/problems/construct-string-with-repeat-limit/description/
class Solution:
  def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
    res = ''
    cnt = collections.Counter(s)

    while True:
      addOne = res and self.helpCheckAddOne(res, cnt)
      c = self.helpGetLargestChar(res, cnt)
      if c == ' ':
        break
      repeats = 1 if addOne else min(cnt[c], repeatLimit)
      res += c * repeats
      cnt[c] -= repeats

    return res

  def helpCheckAddOne(self, res: str, cnt: collections.Counter) -> bool:
    for c in reversed(string.ascii_lowercase):
      if cnt[c]:
        return res[-1] == c
    return False

  def helpGetLargestChar(self, res: str, cnt: collections.Counter) -> int:
    for c in reversed(string.ascii_lowercase):
      if cnt[c] and (not res or res[-1] != c):
        return c
    return ' '