# LeetCode 2070 : Most Beautiful Item for Each Query
# https://leetcode.com/problems/most-beautiful-item-for-each-query/description/
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        prcs, bties = zip(*sorted(items))
        maxBtyUpto = [0] * (len(bties) + 1)

        for i, bty in enumerate(bties):
            maxBtyUpto[i + 1] = max(maxBtyUpto[i], bty)

        return [maxBtyUpto[bisect_right(prcs, query)] for query in queries]