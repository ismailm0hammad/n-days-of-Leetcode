# LeetCode 1957 : Delete Characters to Make Fancy String
# https://leetcode.com/problems/delete-characters-to-make-fancy-string/description/
class Solution:
  def makeFancyString(self, s: str) -> str:
    res=''
    for i in range(len(s)):
        if i<2 or (s[i]!=s[i-1] or s[i]!=s[i-2]):
            res+=s[i]
    return res