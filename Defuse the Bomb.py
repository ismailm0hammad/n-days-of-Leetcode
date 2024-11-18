# LeetCode 1652 : Defuse the Bomb
# https://leetcode.com/problems/defuse-the-bomb/description/
class Solution:
  def decrypt(self, code: list[int], k: int) -> list[int]:
    n = len(code)
    res = [0] * n
    if k == 0:
      return res

    curr_sum = 0
    begin = 1 if k > 0 else n + k  
    end = k if k > 0 else n - 1  

    for i in range(begin, end + 1):
      curr_sum += code[i]

    for i in range(n):
      res[i] = curr_sum
      curr_sum -= code[begin % n]
      begin += 1
      end += 1
      curr_sum += code[end % n]

    return res