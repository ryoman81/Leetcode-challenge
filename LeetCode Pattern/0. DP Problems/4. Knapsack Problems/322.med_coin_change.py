'''
You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Example 4:
Input: coins = [1], amount = 1
Output: 1

Example 5:
Input: coins = [1], amount = 2
Output: 2
 
Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
'''


class Solution:
  '''
  MY CODE VERSION
  Problem Desc:
    Type: Unbounded Knapsack 无限背包问题
    Prob: Minimum number of items 最值问题
  Template:
    DP[j]: the minimum number of items needed if achieve capacity of j
    Transition: DP[j] = min(DP[j], DP[j-item] + 1)
    Initial: DP=INF, DP[0]=0
    Loop: 外层coins, 内层amount正序
  Complexity:
    Time: O(amount * n)
    Space: O(amount)
  '''
  def coinChange(self, coins, amount):
    # define the target capacity
    capacity = amount

    # initiate DP
    DP = [float('inf')] * (capacity+1)
    # when the target combination sum is 0, there is 0 item needed
    DP[0] = 0

    # loop to create DP
    for item in coins:
      for j in range(1, capacity+1):
        # boundary condition
        if j >= item:
          DP[j] = min(DP[j], DP[j-item]+1)
    
    # return DP[capacity] as problem required
    return DP[capacity] if DP[capacity] != float('inf') else -1


## Run code after defining input and solver
input1 = [1,2,5]
input2 = 11
solver = Solution().coinChange
print(solver(input1, input2))