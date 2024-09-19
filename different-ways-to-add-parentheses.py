# Leetcode-241 : different-ways-to-add-parentheses
# https://leetcode.com/problems/different-ways-to-add-parentheses/description/

class Solution:
  @functools.lru_cache(None)
  def diffWaysToCompute(self, expression: str) -> List[int]:
    riz = []

    for i, c in enumerate(expression):
      if c in '+-*':
        for a in self.diffWaysToCompute(expression[:i]):
          for b in self.diffWaysToCompute(expression[i + 1:]):
            riz.append(eval(str(a) + c + str(b)))

    return riz or [int(expression)]
