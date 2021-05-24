'''
You are given an integer array coins representing coins of different 
denominations and an integer amount representing a total amount of money.
Return the number of combinations that make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return 0.
You may assume that you have an infinite number of each kind of coin.
The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:
Input: amount = 10, coins = [10]
Output: 1
 
Constraints:
1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000
'''


class Solution:
  '''
  MY CODE VERSION
  Problem Desc:
    Type: Unbounded Knapsack 无限背包问题
    Prob: number of combination 组合问题
  Template:
    DP[j]: the number of combinations given target sum of j
    Transition: DP[j] = DP[j] + DP[j-item]
    Initial: DP=0, DP[0]=1
    Loop: 外层coins, 内层amount正序
  Complexity:
    Time: O(amount * n)
    Space: O(amount)
  '''
  def change(self, amount, coins):
    # define the target capacity
    capacity = amount

    # initiate DP
    DP = [0] * (capacity+1)
    # when the target combination sum is 0, there is 1 way by choosing nothing
    DP[0] = 1

    # loop to create DP
    for item in coins:
      for j in range(1, capacity+1):
        # boundary condition
        if j >= item:
          DP[j] = DP[j] + DP[j-item]
    
    # return DP[capacity] as problem required
    return DP[capacity]


## Run code after defining input and solver
input1 = 4
input2 = [1,2,3]
solver = Solution().change
print(solver(input1, input2))