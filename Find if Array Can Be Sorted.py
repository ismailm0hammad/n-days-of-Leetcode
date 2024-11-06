# LeetCode 3011 : Find if Array Can Be Sorted
# https://leetcode.com/problems/find-if-array-can-be-sorted/description/
import math

class Solution:
    def canSortArray(self, nums: list[int]) -> int:
        prvSetBits = 0
        prvMax = -math.inf
        crntMax = -math.inf
        crntMin = math.inf

        for num in nums:
            setBits = num.bit_count()
            if setBits != prvSetBits:
                if prvMax > crntMin:
                    return False
                prvSetBits = setBits
                prvMax = crntMax
                crntMax = num
                crntMin = num
            else:
                crntMax = max(crntMax, num)
                crntMin = min(crntMin, num)

        return prvMax <= crntMin