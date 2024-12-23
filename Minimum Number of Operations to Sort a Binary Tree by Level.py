# LeetCode 471 : Minimum Number of Operations to Sort a Binary Tree by Level
# https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/description/
class Solution:
    def minimumOperations(self, root):
        if not root:
            return 0
        
        from collections import deque
        q = deque([root])
        ops = 0

        while q:
            size = len(q)
            lvl = []

            for _ in range(size):
                node = q.popleft()
                lvl.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            sort_level = sorted(lvl)
            mp = {v: i for i, v in enumerate(lvl)}

            for i in range(len(lvl)):
                while lvl[i] != sort_level[i]:
                    ops += 1
                    cur = mp[sort_level[i]]
                    mp[lvl[i]] = cur
                    lvl[i], lvl[cur] = lvl[cur], lvl[i]

        return ops