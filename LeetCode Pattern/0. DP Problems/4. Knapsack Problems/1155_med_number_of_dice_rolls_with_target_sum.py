'''
You have d dice, and each die has f faces numbered 1, 2, ..., f.
Return the number of possible ways (out of fd total ways) 
modulo 10^9 + 7 to roll the dice so the sum of the face up numbers equals target.

Example 1:
Input: d = 1, f = 6, target = 3
Output: 1
Explanation: 
You throw one die with 6 faces.  There is only one way to get a sum of 3.

Example 2:
Input: d = 2, f = 6, target = 7
Output: 6
Explanation: 
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.

Example 3:
Input: d = 2, f = 5, target = 10
Output: 1
Explanation: 
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.

Example 4:
Input: d = 1, f = 2, target = 3
Output: 0
Explanation: 
You throw one die with 2 faces.  There is no way to get a sum of 3.

Example 5:
Input: d = 30, f = 30, target = 500
Output: 222616187
Explanation: 
The answer must be returned modulo 10^9 + 7.

Constraints:
1 <= d, f <= 30
1 <= target <= 1000
'''


class Solution:
  '''
  TEMPLATE VERSION
  Problem Definition:
    该问题是所有背包问题更延展的形式, 叫做分组背包问题. 
    分组背包问题特性是, 多个物品被划分在了多个组别里面, 在单个组别内各物品互斥
    常见方法是在DP当中新开一维度, 表示当前组别, 就本题而言
      - 组别: 色子, [1, d]
      - items: 色子的面, [1, f]
      - capacity: target
    这类问题, 最外层循环组别, 内层按照背包类型和问题类型构建
  Problem Desc:
    Type: 0/1 Knapsack 0/1背包问题 分组化版本
    Prob: maximum of combinations in order 带排序的组合问题
  Template:
    DP[i][j]: the maximum combination with i groups and capacity of j
    Transition: DP[i][j] = DP[i][j] + DP[i-di][j-item]
    Initial: DP=0, DP[0][0]=1
    Loop: 最外层d; 内部常规: 外层capacity, 内层items
  Complexity:
    Time: O(d * f * target)
    Space: O(d * target)
  '''
  def numRollsToTarget(self, d, f, target):
    # define the target capacity
    capacity = target

    # initiate DP
    DP = [[0] * (capacity+1) for _ in range(d+1)]
    # with no dice and 0 capacity, there is one solution
    DP[0][0] = 1

    # loop to create DP
    # outside loop over all groups aka the dices
    for i in range(1, d+1):
      # inside loop is the same as template of combination in order
      for j in range(1, capacity+1):
        for item in range(1, f+1):
          # boundary condition
          if j >= item:
            # modulo by 10**9 + 7 as problem asked
            DP[i][j] = (DP[i][j] + DP[i-1][j-item]) % (10**9 + 7) 

    # return DP[d][capacity] as problem required
    return DP[d][capacity]

  '''
  PREVIOUS VERSION
  Thought:
    Dynamic Programming template:
      State: DP[i][j] - we have through i dices, and the current sum is j
        * Please noted: this time the i and j have very clear practical meaning
                        we want to make the indexing system consistent with this meaning
                        Hence, after initialization, we see the DP is one space larger 
                        as well as in the for-loop
                        because index 0 has no meaning, while index 1 is usually the starting position
      Transition: DP[i][j] = DP[i-1][j-1] + DP[i-1][j-2] + ... + DP[i-1][j-f]
      Initial states: 
        - DP[1][k] = 1 where 1<=k<=min(target, f)
        - This means that we throw dice once, we have one possible way to get number k
        - The maximum k should be of either target value or f, depends on the minimum one
  Complexity:
    Time: O(d*target*f)
    Space: O(d*target) - space optimization available
  '''
  def numRollsToTarget0(self, d, f, target):
    # Define the state
    # We create a (d+1) X (target+1) DP matrix which one space more in each dimension
    # since we want the index is the same as we defined
    DP = [[0] * (target+1) for i in range(d+1)]

    # Initialize the state
    for j in range(1, min(target, f)+1):
      DP[1][j] = 1

    # bottom-up to construct DP
    # loop outlayer: number of dices throwed, from 2 to d times
    for i in range(2, d+1):
      # loop midlayer: current sum of all dices, from i to f*i (possible min and max)
      for j in range(i, target+1):
        # loop inner layer: transition equation from i-1 to i
        for k in range(1, f+1):
          if j-k < 0: break
          DP[i][j] = (DP[i][j] + DP[i-1][j-k]) % (10**9 + 7)
      
    return DP[d][target]

## Run code after defining input and solver
input1 = 2
input2 = 6
input3 = 7
solver = Solution().numRollsToTarget
print(solver(input1, input2, input3))