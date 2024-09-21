# LeetCode 386 - lexicographical-numbers
# https://leetcode.com/problems/lexicographical-numbers/description/
class Solution:
  def lexicalOrder(self, n: int) -> list[int]:
    riz = []
    crn = 1

    while len(riz) < n:
      riz.append(crn)
      if crn * 10 <= n:
        crn *= 10
      else:
        while crn % 10 == 9 or crn == n:
          crn //= 10
        crn += 1

    return riz