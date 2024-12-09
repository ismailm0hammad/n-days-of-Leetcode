# LeetCode 3152 : Special Array II
# https://leetcode.com/problems/special-array-ii/description/
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        res = []
        id = 0
        parityIds = [id]
    
        for a, b in itertools.pairwise(nums):
          if a % 2 == b % 2:
            id += 1
          parityIds.append(id)
    
        for _from, to in queries:
          res.append(parityIds[_from] == parityIds[to])
    
        return res