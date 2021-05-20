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
  Thought:
    Dynamic Programming template:
      State: DP[n] - the minimum number of coins when the sum amount is n
      Transition: DP[i] = min(DP[i-coins[j]]) + 1
      Initial states: DP[0] = 0 - when amount is 0, no coins needed 
  Complexity:
    Time: O(amount * nCoins)
    Space: O(amount) - space optimization available
  '''
  def coinChange1(self, coins, amount):
    n = len(coins)
    
    DP = [float('inf')] * (amount+1)
    DP[0] = 0

    for i in range(1, n+1):
      for j in range(coins[i-1], amount+1):
        DP[j] = min(DP[j], DP[j-coins[i-1]]+1)

    return DP[amount] if DP[amount]!=float('inf') else -1

  '''
  MY CODE VERSION
  Thought:
    Dynamic Programming template:
      State: DP[n] - the minimum number of coins when the sum amount is n
      Transition: DP[i] = min(DP[i-coins[j]]) + 1
      Initial states: DP[0] = 0 - when amount is 0, no coins needed 
  Complexity:
    Time: O(amount * nCoins)
    Space: O(amount) - space optimization available
  '''
  def coinChange(self, coins, amount):
    # Create DP state with 1 x (amount+1)
    DP = [float('inf')] * (amount+1)
    # Initialize DP at 0
    DP[0] = 0

    # Construct DP by looping over amount dollar in range [1, amount]
    for i in range(1, amount+1):
      # an auxiliary variable to find the current minimum DP
      crrMin = float('inf')
      # loop over all coins values
      for val in coins:
        # if out the indexing of DP then continue to the next coin
        if i - val < 0: continue
        # if DP value at i-k is smaller than current min DP then update
        if DP[i-val] < crrMin: 
          crrMin = DP[i-val]
      # after search for all coins, we update DP[i] as transition equation defined
      DP[i] = crrMin + 1

    # finally we return DP value at index of amount.
    # if that value is infinite, we return -1
    # 语义化的Python语法, 看起来真像个句子啊...
    return DP[amount] if DP[amount] != float('inf') else -1


## Run code after defining input and solver
input1 = [1,2,5]
input2 = 11
solver = Solution().coinChange1
print(solver(input1, input2))