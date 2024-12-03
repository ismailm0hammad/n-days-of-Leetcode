# LeetCode 2109 : Adding Spaces to a String
# https://leetcode.com/problems/adding-spaces-to-a-string/description/
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        currentIdx=0
        while spaces:
            spaceIdx=spaces.pop(0)
            while currentIdx!=spaceIdx:
                res+=s[currentIdx]
                currentIdx+=1
            res+=" "
        if currentIdx!=len(s):
            res+=s[currentIdx:]
        return res