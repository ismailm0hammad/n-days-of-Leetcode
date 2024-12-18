# LeetCode 1475 : Final Prices With a Special Discount in a Shop
# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/
class Solution:
  def finalPrices(self, prices: list[int]) -> list[int]:
    res = prices.copy()
    stack = []

    for i, price in enumerate(prices):
      while stack and prices[stack[-1]] >= price:
        res[stack.pop()] -= price
      stack.append(i)

    return res