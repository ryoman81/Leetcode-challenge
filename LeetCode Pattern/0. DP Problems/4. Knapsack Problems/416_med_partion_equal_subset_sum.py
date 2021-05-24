'''
Given a non-empty array nums containing only positive integers, 
find if the array can be partitioned into two subsets such that 
the sum of elements in both subsets is equal.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 
Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100
'''


class Solution:
  '''
  MY CODE VERSION
  Problem Definition:
    如何将该问题成功描述成0/1背包问题是难点. 该问题的思路是:
      - 欲将数组划分成和相等的两部分, 可转换为, 
        是否能从数组中选择部分元素, 他们的和为sum(nums)/2
      - 如果sum(nums)/2为奇数, 那么肯定不能划分成两相等部分
      - 该问题的capacity = sum(nums) / 2
  Problem Desc:
    Type: 0/1 Knapsack 0/1背包问题
    Prob: if exist 存在或组合问题
  Template:
    DP[j]: the number of combinations that meet the requirement at j capacity
    Transition: DP[j] = DP[j] + DP[j-item]
    Initial: DP=0, DP[0]=1
    Loop: 外层nums, 内层capacity倒序
  Complexity:
    Time: O(capacity * n)
    Space: O(capacity)
  '''
  def canPartition(self, nums):
    # 如果数组总和的一半是奇数, 那么不可能分割成两个相等整数
    if sum(nums) % 2: return False

    # define the target capacity
    capacity = int (sum(nums) / 2)

    # initiate DP
    DP = [0] * (capacity+1)
    # when the capacity is 0, there is 1 possibility (by choosing no item)
    DP[0] = 1
    
    # loop to create DP
    for item in nums:
      for j in range(capacity, -1, -1):
        if j >= item:
          DP[j] = DP[j] + DP[j-item]

    # return DP[capacity] as problem required
    return True if DP[capacity]>0 else False


## Run code after defining input and solver
input = [1,1,1,2,3]
solver = Solution().canPartition
print(solver(input))