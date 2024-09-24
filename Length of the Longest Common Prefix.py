# LeetCode 3043 : Find the Length of the Longest Common Prefix
# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/description/

class TrieNode:
  def __init__(self):
    self.children: dict[str, TrieNode] = {}


class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word: str) -> None:
    node: TrieNode = self.root
    for c in word:
      node = node.children.setdefault(c, TrieNode())
    node.isWord = True

  def search(self, word: str) -> int:
    prefixLength = 0
    node = self.root
    for c in word:
      if c not in node.children:
        break
      node = node.children[c]
      prefixLength += 1
    return prefixLength


class Solution:
  def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
    trie = Trie()

    for num in arr1:
      trie.insert(str(num))

    return max(trie.search(str(num)) for num in arr2)