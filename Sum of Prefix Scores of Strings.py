# LeetCode 2416 : Sum of Prefix Scores of Strings
# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/
class TrieNode:
  def __init__(self):
    self.children: dict[str, TrieNode] = {}
    self.count = 0


class Solution:
  def sumPrefixScores(self, words: list[str]) -> list[int]:
    root = TrieNode()

    def insert(word: str) -> None:
      node: TrieNode = root
      for c in word:
        node = node.children.setdefault(c, TrieNode())
        node.count += 1

    for word in words:
      insert(word)

    def getScore(word: str) -> int:
      node: TrieNode = root
      score = 0
      for c in word:
        node = node.children[c]
        score += node.count
      return score

    return [getScore(word) for word in words]