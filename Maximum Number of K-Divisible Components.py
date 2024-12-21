# LeetCode 2872 : Maximum Number of K-Divisible Components
# https://leetcode.com/problems/maximum-number-of-k-divisible-components/description/
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: list[list[int]], values: list[int], k: int) -> int:
        res = 0
        gph = [[] for _ in range(n)]

        def dfs(u, prv):
            nonlocal res
            treeSum = values[u]

            for v in gph[u]:
                if v != prv:
                    treeSum += dfs(v, u)

            if treeSum % k == 0:
                res += 1
            return treeSum

        for u, v in edges:
            gph[u].append(v)
            gph[v].append(u)

        dfs(0, -1)
        return res