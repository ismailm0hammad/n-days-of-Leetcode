# LeetCode 2641 : Cousins in Binary Tree II
# https://leetcode.com/problems/cousins-in-binary-tree-ii/description/
class Solution:
  def replaceValueInTree(self, root: TreeNode | None) -> TreeNode | None:
    levelSums = []

    def dfs(root, level):
      if not root:
        return
      if len(levelSums) == level:
        levelSums.append(0)
      levelSums[level] += root.val
      dfs(root.left, level + 1)
      dfs(root.right, level + 1)

    def replace(root,level, curr,):
      nextLevel = level + 1
      nextLevelCousinsSum = (
          (levelSums[nextLevel] if nextLevel < len(levelSums) else 0) -
          (root.left.val if root.left else 0) -
          (root.right.val if root.right else 0))
      if root.left:
        curr.left = TreeNode(nextLevelCousinsSum)
        replace(root.left, level + 1, curr.left)
      if root.right:
        curr.right = TreeNode(nextLevelCousinsSum)
        replace(root.right, level + 1, curr.right)
      return curr

    dfs(root, 0)
    return replace(root, 0, TreeNode(0))