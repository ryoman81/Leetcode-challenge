'''
You are given an array prices where prices[i] is the price of a given stock on the ith day, 
and an integer fee representing a transaction fee.
Find the maximum profit you can achieve. You may complete as many transactions as you like, 
but you need to pay the transaction fee for each transaction.
Note: You may not engage in multiple transactions simultaneously 
(i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Example 2:
Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6
 
Constraints:
1 <= prices.length <= 5 * 104
1 <= prices[i] < 5 * 104
0 <= fee < 5 * 104
'''


class Solution:
  '''
  SPACE OPTIMIZED VERSION
    since both DP0 and DP1 rely only on the previous state
  Complexity:
    Time: O(n)
    Space: O(1)
  '''
  def maxProfit0(self, prices, fee):
    n = len(prices)
    DP0 = 0
    DP1 = -prices[0]

    for i in range(1, n):
      temp = DP0
      DP0 = max(DP0, DP1+prices[i]-fee)
      DP1 = max(DP1, temp-prices[i])
    
    return DP0

  '''
  TEMPLATE VERSION
    Similar like 121, there is no need to maintain the dimension of k
    since [k] and [k-1] should have no influence on final DP
  Complexity:
    Time: O(n)
    Space: O(2n)
  '''
  def maxProfit1(self, prices, fee):
    n = len(prices)
    # both DP0 and DP1 are only related to the variable of day
    DP0 = [0] * n
    DP1 = [0] * n

    # initialize DP1 at i=0
    DP1[0] = -prices[0]

    # Loop
    for i in range(1, n):
      DP0[i] = max(DP0[i-1], DP1[i-1] + prices[i] - fee)
      DP1[i] = max(DP1[i-1], DP0[i-1]-prices[i])
    
    return DP0[n-1]


## Run code after defining input and solver
input1 = [1,3,2,8,4,9]
input2 = 2
solver = Solution().maxProfit1
print(solver(input1, input2))