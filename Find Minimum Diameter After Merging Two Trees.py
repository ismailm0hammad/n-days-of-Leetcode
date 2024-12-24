# LeetCode 3203 : Find Minimum Diameter After Merging Two Trees
# https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/description/
class Solution:
  def minimumDiameterAfterMerge(self, edges1: list[list[int]], edges2: list[list[int]]) -> int:
    diameter1, diameter2 = self.help_getDiameter(edges1), self.help_getDiameter(edges2)
    return max(diameter1, diameter2, (diameter1 + 1) // 2 + (diameter2 + 1) // 2 + 1)

  def help_getDiameter(self, edges):
    n, graph = len(edges) + 1, [[] for _ in range(len(edges) + 1)]
    for u, v in edges:
      graph[u].append(v)
      graph[v].append(u)
    maxDiameter = [0]
    self.help_maxDepth(graph, 0, -1, maxDiameter)
    return maxDiameter[0]

  def help_maxDepth(self, graph, u, prev, maxDiameter):
    maxSubDepth1, maxSubDepth2 = 0, 0
    for v in graph[u]:
      if v != prev:
        maxSubDepth = self.help_maxDepth(graph, v, u, maxDiameter)
        if maxSubDepth > maxSubDepth1:
          maxSubDepth2, maxSubDepth1 = maxSubDepth1, maxSubDepth
        elif maxSubDepth > maxSubDepth2:
          maxSubDepth2 = maxSubDepth
    maxDiameter[0] = max(maxDiameter[0], maxSubDepth1 + maxSubDepth2)
    return 1 + maxSubDepth1