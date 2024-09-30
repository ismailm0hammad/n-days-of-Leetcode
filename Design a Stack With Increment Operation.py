# LeetCode 138 : Design a Stack With Increment Operation
# https://leetcode.com/problems/design-a-stack-with-increment-operation/description/
class CustomStack:
  def __init__(self, maxSize: int):
    self.maxSize = maxSize
    self.stack = []
    self.rem_increments = []

  def push(self, x: int) -> None:
    if len(self.stack) == self.maxSize:
      return
    self.stack.append(x)
    self.rem_increments.append(0)

  def pop(self) -> int:
    if not self.stack:
      return -1
    if len(self.stack) > 1:
      self.rem_increments[-2] += self.rem_increments[-1]
    return self.stack.pop() + self.rem_increments.pop()

  def increment(self, k: int, val: int) -> None:
    if not self.stack:
      return
    i = min(k - 1, len(self.stack) - 1)
    self.rem_increments[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)