# leetCode 2593 : Find Score of an Array After Marking All Elements
# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/description/
class Solution:
  def findScore(self, nums: list[int]) -> int:
    res = 0
    seen = set()

    for num, i in sorted([(num, i) for i, num in enumerate(nums)]):
      if i in seen:
        continue
      seen.add(i - 1)
      seen.add(i + 1)
      seen.add(i)
      res += num

    return res