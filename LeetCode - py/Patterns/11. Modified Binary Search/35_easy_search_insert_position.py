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
  MY CODE VERSION
  Thought:
    - This is the exact form of binary search template
    - Only change the final returning value if no target found
    - The considering part is what to return if no target found (see comment)
  Complexity:
    Time: O(logn)
    Space: O(1)
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
    # if exthausted while loop: the left point came to the position that ONE STEP LARGET THAN TARGET
    # which means if the target is inserted, it will take this left location!
    return left


## Run code after defining input and solver
input1 = [1,2,3,4,5,6,7,8,9]
input2 = 3.5
solver = Solution().searchInsert
print(solver(input1, input2))