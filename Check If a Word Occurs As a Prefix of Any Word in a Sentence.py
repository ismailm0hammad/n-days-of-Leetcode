# LeetCode 1455 : Check If a Word Occurs As a Prefix of Any Word in a Sentence
# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/description/
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        ptrnLen=len(searchWord)
        for i in range(len(words)):
            if words[i][:ptrnLen]==searchWord:
                return i+1
        return -1