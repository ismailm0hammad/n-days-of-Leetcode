# LeetCode 1346 : Check If N and Its Double Exist
# https://leetcode.com/problems/check-if-n-and-its-double-exist/description/
class Solution:
  def checkIfExist(self, arr: list[int]) -> bool:
    checked = set()

    for a in arr:
      if a * 2 in checked or a % 2 == 0 and a // 2 in checked:
        return True
      checked.add(a)

    return False