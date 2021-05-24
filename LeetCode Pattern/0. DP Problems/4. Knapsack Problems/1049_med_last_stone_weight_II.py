'''
You are given an array of integers stones where 
stones[i] is the weight of the ith stone.
We are playing a game with the stones. On each turn, 
we choose any two stones and smash them together. 
Suppose the stones have weights x and y with x <= y. 
The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and 
the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. 
If there are no stones left, return 0.

Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We can combine 2 and 4 to get 2, so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1, so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1, so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0, so the array converts to [1], then that's the optimal value.

Example 2:
Input: stones = [31,26,33,21,40]
Output: 5

Example 3:
Input: stones = [1,2]
Output: 1
 
Constraints:
1 <= stones.length <= 30
1 <= stones[i] <= 100
'''


class Solution:
  '''
  MY CODE VERSION
  Problem Definition:
    该问题描述会和416非常相似:
      - 问题可转化为, 如何从stones选取items, 使其和最接近于capacity
      - 该问题的capacity为 sum/2
      - 即选取部分items使其总和最接近于capacity, 因此另一部items总和也将接近于capacity
      - 最终将两部分相互碰撞抵消后, 剩余石头重量达到最小
  Problem Desc:
    Type: 0/1 Knapsack 0/1背包问题
    Prob: maximum weight 最值问题
  Template:
    DP[j]: the maximum weight of selected stones when putting into a j size knapsack
    Transition: DP[j] = max(DP[j], DP[j-item] + item)
    Initial: DP=0, DP[0]=0
    Loop: 外层stones, 内层capacity倒序
  Complexity:
    Time: O(capacity * n)
    Space: O(capacity)
  '''
  def lastStoneWeightII(self, stones):
    # define the target capacity
    capacity = int( sum(stones)/2 )

    # initiate DP
    DP = [0] * (capacity+1)
    # when the capacity is 0, there is 0 weight
    DP[0] = 0
    
    # loop to create DP
    for item in stones:
      for j in range(capacity, -1, -1):
        if j >= item:
          DP[j] = max(DP[j], DP[j-item]+item)

    # DP[capacity] 为装入一个 sum/2 大小背包的最大重量
    # 因此另一半的重量即为 sum - DP[capacity] (这一半重量大于等于另一半)
    # 两半相减即为中和掉所有石头后剩余的重量
    return (sum(stones) - DP[capacity]) - DP[capacity]


## Run code after defining input and solver
input = [2,7,4,1,8,1]
solver = Solution().lastStoneWeightII
print(solver(input))