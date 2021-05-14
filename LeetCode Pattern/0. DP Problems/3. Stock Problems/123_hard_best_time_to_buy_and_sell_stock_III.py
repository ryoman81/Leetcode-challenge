'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete at most two transactions.
Note: You may not engage in multiple transactions simultaneously 
(i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Example 4:
Input: prices = [1]
Output: 0
 
Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 105
'''


class Solution:
  '''
  SPACE OPTIMIZED VERSION
    Since k can be 0, 1, or 3, the space simplification cannot as easy as 121 and 122
    We use four variables to replace DP0 and DP1 at k = 1 and k = 2
  Complexity:
    Time: O(n)
    Space: O(1)
  '''
  def maxProfit(self, prices):
    n = len(prices)
    minPrice1 = float('INF')
    maxProfit1 = 0
    minPrice2 = float('INF')
    maxProfit2 = 0

    for i in range(n):
      minPrice1 = min(minPrice1, prices[i])                # the first buying price
      maxProfit1 = max(maxProfit1, prices[i] - minPrice1)  # the first profit after selling
      minPrice2 = min(minPrice2, prices[i] - maxProfit1)   # the second buying price
      maxProfit2 = max(maxProfit2, prices[i] - minPrice2)  # the final profit after selling

    return maxProfit2


  '''
  TEMPLATE VERSION
    This version follows the generalized template strictly
    Let's think about three variables
      - days: [0, n-1]
      - trading times: [0, 2]
      - actions: sell or buy
  Complexity:
    Time: O(n)
    Space: O(4n)
  '''
  def maxProfit2(self, prices):
    n = len(prices)
    # this time we can only trade 1 time, k = 2 (k+1=3)
    DP0 = [[0] * 3 for _ in range(n)]
    DP1 = [[0] * 3 for _ in range(n)]

    # initialize DP0 DP1 at k=0 and i=0
    for i in range(n):
      DP1[i][0] = float('-INF')
    for ki in range(3):
      DP1[0][ki] = -prices[0]

    # Loop
    for i in range(1, n):
      # we no longer need to loop over k because k=2
      DP0[i][1] = max(DP0[i-1][1], DP1[i-1][1]+prices[i])
      DP1[i][1] = max(DP1[i-1][1], DP0[i-1][0]-prices[i])
      DP0[i][2] = max(DP0[i-1][2], DP1[i-1][2]+prices[i])
      DP1[i][2] = max(DP1[i-1][2], DP0[i-1][1]-prices[i])

    return DP0[n-1][2]


## Run code after defining input and solver
input = [7,6,4,6,8,3]
solver = Solution().maxProfit
print(solver(input))