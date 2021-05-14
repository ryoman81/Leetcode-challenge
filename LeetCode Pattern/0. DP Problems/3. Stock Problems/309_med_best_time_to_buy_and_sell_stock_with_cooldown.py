'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete as many transactions as you like 
(i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously 
(i.e., you must sell the stock before you buy again). 

Example 1:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:
Input: prices = [1]
Output: 0
 
Constraints:
1 <= prices.length <= 5000
0 <= prices[i] <= 1000
'''


class Solution:
  '''
  SPACE OPTIMIZED VERSION
    Modified where we maintain an additional temp varible to record the profit one day before
  Complexity:
    Time: O(n)
    Space: O(1)
  '''
  def maxProfit0(self, prices):
    n = len(prices)
    DP0 = 0
    DP1 = -prices[0]
    before = 0

    for i in range(1, n):
      temp = DP0
      DP0 = max(DP0, DP1+prices[i])
      DP1 = max(DP1, before-prices[i])
      before = temp
    
    return DP0

  '''
  TEMPLATE VERSION
    A class of problems like 122 and 714
    Transition a little differ where
      DP1[i] = max(DP1[i-1], DP0[i-2] - prices[i])
      because we have a one-day cooldown, if DP1 transit from DP0, it should be two day before
  Complexity:
    Time: O(n)
    Space: O(2n)
  '''
  def maxProfit1(self, prices):
    n = len(prices)
    # both DP0 and DP1 are only related to the variable of day
    DP0 = [0] * n
    DP1 = [0] * n

    # initialize DP1 at i=0
    DP1[0] = -prices[0]

    # Loop
    for i in range(1, n):
      DP0[i] = max(DP0[i-1], DP1[i-1] + prices[i])
      DP1[i] = max(DP1[i-1], DP0[i-2] - prices[i])
    
    return DP0[n-1]


## Run code after defining input and solver
input1 = [1,2,3,0,2]
solver = Solution().maxProfit1
print(solver(input1))