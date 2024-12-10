# LeetCode 2981 : Find Longest Special Substring That Occurs Thrice I
# https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/description/
class Solution:
  def maximumLength(self, s: str) -> int:
    n = len(s)
    curLen = 0
    prvLtr = '@'
    counts = [[0] * (n + 1) for _ in range(26)]

    for c in s:
      if c == prvLtr:
        curLen += 1
        counts[string.ascii_lowercase.index(c)][curLen] += 1
      else:
        curLen = 1
        counts[string.ascii_lowercase.index(c)][curLen] += 1
        prvLtr = c

    def getMaxFreq(count):
      reps = 0
      for freq in range(n, 0, -1):
        reps += count[freq]
        if reps >= 3:
          return freq
      return -1

    return max(getMaxFreq(count) for count in counts)