# LeetCode 515 : Find Largest Value in Each Tree Row
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
class Solution:
  def largestValues(self, root: TreeNode | None) -> list[int]:
    if not root:
      return []

    res = []
    q = collections.deque([root])

    while q:
      mx = -math.inf
      for _ in range(len(q)):
        root = q.popleft()
        mx = max(mx, root.val)
        if root.left:
          q.append(root.left)
        if root.right:
          q.append(root.right)
      res.append(mx)

    return res