# LeetCode 2097 : Valid Arrangement of Pairs
# https://leetcode.com/problems/valid-arrangement-of-pairs/description/
class Solution:
  def validArrangement(self, pairs: list[list[int]]) -> list[list[int]]:
    res = []
    gph = collections.defaultdict(list)
    outDgri = collections.Counter()
    inDgri = collections.Counter()

    for start, end in pairs:
      gph[start].append(end)
      outDgri[start] += 1
      inDgri[end] += 1

    def getStartNode() -> int:
      for u in gph.keys():
        if outDgri[u] - inDgri[u] == 1:
          return u
      return pairs[0][0]

    def eulerPath(u):
      stack = gph[u]
      while stack:
        v = stack.pop()
        eulerPath(v)
        res.append([u, v])

    eulerPath(getStartNode())
    return res[::-1]