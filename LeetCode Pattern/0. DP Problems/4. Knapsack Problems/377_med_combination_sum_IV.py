'''
Given an array of distinct integers nums and a target integer target, 
return the number of possible combinations that add up to target.
The answer is guaranteed to fit in a 32-bit integer.

Example 1:
Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.

Example 2:
Input: nums = [9], target = 3
Output: 0
 
Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000
'''


class Solution:
  '''
  MY CODE VERSION
  Problem Definition:
    这是第一道涉及到排序的背包问题, 背包本身属于无限背包
    但凡所有的为排列后的组合问题, 内外层循环需要颠倒 (自己还未证明)
  Problem Desc:
    Type: Unbounded Knapsack 无限背包问题
    Prob: number of combinations with order 排序问题
  Template:
    DP[j]: the number of combinations that sum up to j
    Transition: DP[j] = DP[j] + DP[j-item]
    Initial: DP=0, DP[0]=1
    Loop: 外层capacity, 内层item
  Complexity:
    Time: O(target * n)
    Space: O(target)
  '''
  def combinationSum4(self, nums, target):
    # define the target capacity
    capacity = target

    # initiate DP
    DP = [0] * (capacity+1)
    # when the target combination sum is 0, there is 1 solution
    DP[0] = 1

    # loop to create DP
    for j in range(1, capacity+1):
      for item in nums:
        # boundary condition
        if j >= item:
          DP[j] = DP[j] + DP[j-item]
    
    # return DP[capacity] as problem required
    return DP[capacity]


## Run code after defining input and solver
input1 = [1,2,3]
input2 = 4
solver = Solution().combinationSum4
print(solver(input1, input2))