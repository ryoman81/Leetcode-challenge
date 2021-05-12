'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock 
and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 
Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
'''


class Solution:
  '''
  SPACE OPTIMIZED VERSION
    This solution is exactly the solution from LeetCode
    好多人留言说这不是DP题目. 事实上, 这个解就是最初template解法一步步优化而成的
    - DP0 --> maxProfit   :: 最大化收益
    - DP1 --> minPrice    :: 这里做了变换, minPrice已经不是DP1, 即前一天手头握有股票的价格了
  Complexity:
    Time: O(n)
    Space: O(1)
  '''
  def maxProfit(self, prices):
    maxProfit = 0
    minPrice = prices[0]
  
    for i in range(1, len(prices)):
      minPrice = min(minPrice, prices[i])
      maxProfit = max(maxProfit, prices[i]-minPrice)

    return maxProfit

  '''
  SPACE OPTIMIZED VERSION
    since both DP0 and DP1 rely only on the previous state
    因此DP当中常见的传统的空间优化可以实施, 将DP0[i] 和 DP1[i]用单个变量表达
  Complexity:
    Time: O(n)
    Space: O(1)
  '''
  def maxProfit0(self, prices):
    n = len(prices)
    DP0 = 0
    DP1 = -prices[0]

    for i in range(1, n):
      DP0 = max(DP0, DP1+prices[i])
      DP1 = max(DP1, -prices[i])
    
    return DP0

  '''
  OPTIMIZED VERSION
    Since k=0, there is no need to maintain the dimension of k
    Lets think about the state transition and initialization
      - Transition: 
        DP0 relies on the previous DP0 or DP1 no matter what k is
          所以直接把k这个维度去除掉就可以了
        DP1 relies previous DP1[k] or DP0[k-1]. However, since k=1
          如果DP1是从前一个DP0转移过来, 则前一个DP0一定为0. 动脑筋
  Complexity:
    Time: O(n)
    Space: O(2n)
  '''
  def maxProfit1(self, prices):
    n = len(prices)
    # both DP0 and DP1 are only related to the variable of day
    DP0 = [0] * n
    DP1 = [0] * n

    # initialize DP0 DP1 at i=0
    # think that if we hold a stock at i=0
    DP1[0] = -prices[0]

    # Loop
    for i in range(1, n):
      DP0[i] = max(DP0[i-1], DP1[i-1] + prices[i])
      DP1[i] = max(DP1[i-1], -prices[i])
    
    return DP0[n-1]

  '''
  TEMPLATE VERSION
    This version follows the generalized template strictly
    Let's think about three variables
      - days: [0, n-1]
      - actions: sell or buy
      - trading times: k = 1
  Complexity:
    Time: O(n)
    Space: O(4n)
  '''
  def maxProfit2(self, prices):
    n = len(prices)
    # this time we can only trade 1 time, k = 1
    DP0 = [[0] * 2 for _ in range(n)]
    DP1 = [[0] * 2 for _ in range(n)]

    # initialize DP0 DP1 at k=0 and i=0
    for i in range(n):
      DP1[i][0] = float('-INF')
    for ki in range(2):
      DP1[0][ki] = -prices[0]

    # Loop
    for i in range(1, n):
      # we no longer need to loop over k because k=1
      DP0[i][1] = max(DP0[i-1][1], DP1[i-1][1]+prices[i])
      DP1[i][1] = max(DP1[i-1][1], DP0[i-1][0]-prices[i])
    
    return DP0[n-1][1]


## Run code after defining input and solver
input = [7,6,4,6,8,3]
solver = Solution().maxProfit0
print(solver(input))