# leetCode 2583 : Kth Largest Sum in a Binary Tree
# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def kthLargestLevelSum(self, root: TreeNode | None, k: int) -> int:
    lvlSms = []

    def dfs(root, lvl):
      if not root:
        return
      if len(lvlSms) == lvl:
        lvlSms.append(0)
      lvlSms[lvl] += root.val
      dfs(root.left, lvl + 1)
      dfs(root.right, lvl + 1)

    dfs(root, 0)
    if len(lvlSms) < k:
      return -1

    return sorted(lvlSms, reverse=True)[k - 1]