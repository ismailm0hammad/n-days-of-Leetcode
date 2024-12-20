# leetCode 2415 : Reverse Odd Levels of Binary Tree
# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/
class Solution:
  def reverseOddLevels(self, root: TreeNode | None) -> TreeNode | None:
    def dfs(left: TreeNode | None, right: TreeNode | None, isOddLevel: bool) -> None:
      if not left:
        return
      if isOddLevel:
        left.val, right.val = right.val, left.val
      dfs(left.left, right.right, not isOddLevel)
      dfs(left.right, right.left, not isOddLevel)

    dfs(root.left, root.right, True)
    return root