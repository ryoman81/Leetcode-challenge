'''
You are given an integer array nums sorted in ascending order (with distinct values), and an integer target.
Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
If target is found in the array return its index, otherwise, return -1.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Constraints:
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is guaranteed to be rotated at some pivot.
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
  def search(self, nums, target):
    left = 0
    right = len(nums) - 1

    while (left <= right):
      mid = (left + right) // 2
      if (nums[mid] == target): 
        return mid

      # the left is sorted
      if (nums[left] <= nums[mid]):
        if (nums[left] <= target and target < nums[mid]):
          right = mid - 1
        else:
          left = mid + 1
      # the right is sorted
      else:
        if (nums[mid] < target and target <= nums[right]):
          left = mid + 1
        else:
          right = mid - 1

    return -1


## Run code after defining input and solver
input1 = [4,5,6,7,8,9,10,11,0,1,2,3]
input2 = 1
solver = Solution().search
print(solver(input1, input2))