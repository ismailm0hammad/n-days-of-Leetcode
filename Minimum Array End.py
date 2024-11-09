# LeetCode 3133 : Minimum Array End
# https://leetcode.com/problems/minimum-array-end/description/
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        kMaxBit = n.bit_length() + x.bit_length()
        k = n - 1
        kBnryIdx = 0

        for i in range(kMaxBit):
            if x >> i & 1 == 0:
                if k >> kBnryIdx & 1:
                    x |= 1 << i
                kBnryIdx += 1

        return x
