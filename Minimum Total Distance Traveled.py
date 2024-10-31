# LeetCode 2463 : Minimum Total Distance Traveled
# https://leetcode.com/problems/minimum-total-distance-traveled/description/
class Solution:
  def minimumTotalDistance(self,robot: list[int],factory: list[list[int]],) -> int:
    robot.sort()
    factory.sort()

    @functools.lru_cache(None)
    def dp(i, j, k):
      if i == len(robot):
        return 0
      if j == len(factory):
        return math.inf
      skipFctry = dp(i, j + 1, 0)
      pos, lmt = factory[j]
      useFctry = (dp(i + 1, j, k + 1) + abs(robot[i] - pos)if lmt > k else math.inf)
      return min(skipFctry, useFctry)

    return dp(0, 0, 0)