# LeetCode 2490 : Circular Sentence
# https://leetcode.com/problems/circular-sentence/description/
class Solution:
  def isCircularSentence(self, sentence: str) -> bool:
    for i, c in enumerate(sentence):
      if c == ' ' and sentence[i - 1] != sentence[i + 1]:
        return False
    return sentence[0] == sentence[-1]