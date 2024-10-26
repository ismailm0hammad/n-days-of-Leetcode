# LeetCode 2458 : Height of Binary Tree After Subtree Removal Queries
# https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/description/?

class Solution:
  def treeQueries(self, root: TreeNode | None, queries: list[int]) -> list[int]:
    @lru_cache(None)
    def height(root):
      if not root:
        return 0
      return 1 + max(height(root.left), height(root.right))

    valToMaxHeight = {}

    def dfs(root, depth, maxHeight):
      if not root:
        return
      valToMaxHeight[root.val] = maxHeight
      dfs(root.left, depth + 1, max(maxHeight, depth + height(root.right)))
      dfs(root.right, depth + 1, max(maxHeight, depth + height(root.left)))

    dfs(root, 0, 0)
    return [valToMaxHeight[query] for query in queries]