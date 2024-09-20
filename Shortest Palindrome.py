# LeetCode 214 : Shortest Palindrome
# https://leetcode.com/problems/shortest-palindrome/description/

class Solution:
  def shortestPalindrome(self, s: str) -> str:
    rev = s[::-1]

    for i in range(len(rev)):
      if s.startswith(rev[i:]):
        return rev[:i] + s

    return rev + s