# Leetcode 2516 : Take K of Each Character From Left and Right
# https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/description/
class Solution:
  def takeCharacters(self, s: str, k: int) -> int:
    n = len(s)
    res = n
    count = collections.Counter(s)
    if any(count[c] < k for c in 'abc'):
      return -1

    l = 0
    for r, c in enumerate(s):
      count[c] -= 1
      while count[c] < k:
        count[s[l]] += 1
        l += 1
      res = min(res, n - (r - l + 1))

    return res