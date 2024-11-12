# LeetCode 2601 : Prime Subtraction Operation
# https://leetcode.com/problems/prime-subtraction-operation/description/
class Solution:
  def primeSubOperation(self, nums: list[int]) -> bool:
    kMax = 1000
    primes = self.helpSieveEratosthenes(kMax)

    prvNum = 0
    for num in nums:
      i = bisect.bisect_left(primes, num - prvNum)
      if i > 0:
        num -= primes[i - 1]
      if num <= prvNum:
        return False
      prvNum = num

    return True

  def helpSieveEratosthenes(self, n):
    isPrime = [True] * n
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, int(n**0.5) + 1):
      if isPrime[i]:
        for j in range(i * i, n, i):
          isPrime[j] = False
    return [i for i in range(n) if isPrime[i]]