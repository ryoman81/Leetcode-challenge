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
  Problem Definition:
    如何将该问题成功描述成0/1背包问题比前者案例416还要麻烦, 我们需要先设立一下数学推导:
      - 假设在一个成功的正负数相加的组合当中,
      - 其中, 所有正数之和为 X, 所有负数的绝对值之和为 Y
      - 那么输入参数即所有正负数之和为 target = X-Y
      - 所有数值之和即所有数值的绝对值之和为 sum = X + Y
      - 因此可以推导出表达式 X = (target + sum) / 2
      - 最终, X有个显性的意义, 即从nums选中若干个items, 它们的和为X, 此题目立即转换为416
      - Finally, we define X = capacity
  Problem Desc:
    Type: 0/1 Knapsack 0/1背包问题
    Prob: number of combination 组合问题
  Template:
    DP[j]: the number of combinations that meet the requirement at j capacity
    Transition: DP[j] = DP[j] + DP[j-item]
    Initial: DP=0, DP[0]=1
    Loop: 外层nums, 内层capacity倒序
  Complexity:
    Time: O(capacity * n)
    Space: O(capacity)
  '''
  def findTargetSumWays(self, nums, target):
    # 所有正数之和, X, 不可能小于target, 因此 X >= target
    if (target+sum(nums))/2 < target: return 0
    # 所有正数之和*2 不可能是奇数 (因为任何数字x2之后都不能是奇数)
    # 此处是本题最难想到的一个边界条件. 十分难理解, 但没有的话会不通过
    if (target+sum(nums))%2: return 0

    # define the target capacity
    capacity = int ((target+sum(nums))/2)

    # initiate DP
    DP = [0] * (capacity+1)
    # when the target combination sum is 0, there is 0 item needed
    DP[0] = 1

    # loop to create DP
    for item in nums:
      for j in range(capacity, -1, -1):
        # boundary condition
        if j >= item:
          DP[j] = DP[j] + DP[j-item]
    
    # return DP[capacity] as problem required
    return DP[capacity]


## Run code after defining input and solver
input1 = [7,9,3,8,0,2,4,8,3,9]
input2 = 0
solver = Solution().findTargetSumWays
print(solver(input1, input2))