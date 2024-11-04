# LeetCode 3163 : String Compression III
# https://leetcode.com/problems/string-compression-iii/description/
class Solution:
  def compressedString(self, word: str) -> str:
    n = len(word)
    riz = []
    i = 0
    j = 0

    while i < n:
      count = 0
      while j < n and word[j] == word[i] and count < 9:
        j += 1
        count += 1
      riz.append(str(count) + word[i])
      i = j

    return ''.join(riz)