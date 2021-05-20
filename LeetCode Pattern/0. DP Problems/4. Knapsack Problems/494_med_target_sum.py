'''
You are given an integer array nums and an integer target.
You want to build an expression out of nums by adding one of the symbols '+' and '-' 
before each integer in nums and then concatenate all the integers.
For example, if nums = [2, 1], you can add a '+' before 2 and 
a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Example 1:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:
Input: nums = [1], target = 1
Output: 1

Constraints:
1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    Type: 0/1 Knapsack Problem; fulfill the knapsack (完全装满类型)
    Definition: 
      - 
    DP template:
      - DP[i][j]: the max number of possible solutions of adding up to j with i个 numbers
      - Transition: DP[i][j] = DP[i-1][j-nums[i-1]] + DP[i-1][j+nums[i-1]]
        -> 0 <= i <= n           // n numbers in total
        -> -cap <= j <= cap      // the range of sum
      - Init: DP = 0, DP[i][nums[0]] = 1, DP[i][-nums]
  Complexity:
    Time: O()
    Space: O()
  '''
  def findTargetSumWays0(self, nums, target):
    n = len(nums)
    cap = sum(nums)

    if cap < target or target < -cap:
      return 0

    DP = [0] * (cap*2+1)
    DP[cap] = 1

    for i in range(1, n+1):
      temp = [0] * (cap*2+1)
      for j in range(nums[i-1], cap*2+1-nums[i-1]):
        if j-nums[i-1] >= 0:
          temp[j] += DP[j-nums[i-1]]
        if j+nums[i-1] <= cap*2:  
          temp[j] += DP[j+nums[i-1]]
      DP = temp

    return DP[target+cap]


  '''
  MY CODE VERSION
  Thought:
    Type: 0/1 Knapsack Problem; fulfill the knapsack (完全装满类型)
    Definition: 
      - 
    DP template:
      - DP[i][j]: the max number of possible solutions of adding up to j with i个 numbers
      - Transition: DP[i][j] = DP[i-1][j-nums[i-1]] + DP[i-1][j+nums[i-1]]
        -> 0 <= i <= n           // n numbers in total
        -> -cap <= j <= cap      // the range of sum
      - Init: DP = 0, DP[i][nums[0]] = 1, DP[i][-nums]
  Complexity:
    Time: O()
    Space: O()
  '''
  def findTargetSumWays(self, nums, target):
    n = len(nums)
    cap = sum(nums)

    if cap < target or target < -cap:
      return 0

    DP = [[0] * (cap*2+1) for _ in range(n+1)]
    DP[0][cap] = 1

    for i in range(1, n+1):
      for j in range(0, cap*2+1):
        if j-nums[i-1] >= 0:
          DP[i][j] += DP[i-1][j-nums[i-1]]
        if j+nums[i-1] <= cap*2:  
          DP[i][j] += DP[i-1][j+nums[i-1]]
    
    return DP[n][target+cap]

## Run code after defining input and solver
input1 = [1,1,1,1,1]
input2 = 3
solver = Solution().findTargetSumWays
print(solver(input1, input2))