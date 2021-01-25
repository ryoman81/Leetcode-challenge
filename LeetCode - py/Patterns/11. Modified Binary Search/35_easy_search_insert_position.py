'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
 
Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
'''


class Solution:
  '''
  THE OPTIMAL CODE VERSION
  Improvement:
    1.
  Thought:
    1.  
  Complexity:
    Time: O()
    Space: O()
  '''
  def functionOpt(self):
    return 0

  '''
  MY CODE VERSION
  Thought:
    1. 
  Complexity:
    Time: O()
    Space: O()
  '''
  def searchInsert(self, nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
      mid = left + (right-left)//2
      if nums[mid] == target:
        return mid
      elif nums[mid] < target:
        left = mid + 1
      else:
        right = mid - 1

    return left


## Run code after defining input and solver
input1 = [1,3,5,6]
input2 = 0
solver = Solution().searchInsert
print(solver(input1, input2))