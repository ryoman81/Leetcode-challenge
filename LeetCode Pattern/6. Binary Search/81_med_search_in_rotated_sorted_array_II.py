'''
You are given an integer array nums sorted in ascending order (not necessarily distinct values), and an integer target.
Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,4,4,5,6,6,7] might become [4,5,6,6,7,0,1,2,4,4]).
If target is found in the array return its index, otherwise, return -1.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
 
Constraints:
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104
'''


class Solution:
  '''
  THE OPTIMAL CODE VERSION
  Improvement:
    Similar to the problem 33, but we cannot compare mid to left
      - because if mid == left, we cannot guarantee the left is sorted
        a) mid overlaps with left like in 33
        b) mid duplicate to the left e.g. [1,0,1,1,1]
    Then we choose to compare with right and the problem becomes a 母集 of 33
  Thought:
    1. similar to 33 compare mid to right
    2. if not success, distinguish the other two scenarios if mid > right or mid = right
    3. if mid = right: it indicates that there must be a duplicate between right and left [1,0,1,1,1] or [1,1,1,0,1]
       no guarantee which side is sorted, then no action to make that narrows down the window in half
  Complexity:
    Time: O(logn)   think if there exists O(n)? I don't think so, because move right--, the mid will change
    Space: O(1)
  '''
  def search(self, nums, target):
    left = 0
    right = len(nums) - 1

    while (left <= right):
      mid = left + (right - left) // 2
      if (nums[mid] == target): 
        return True

      # compare to the right and divided into three scenarios
      if nums[mid] < nums[right]:
        # in this case, the right must be sorted
        if nums[mid] < target <= nums[right]:
          left = mid + 1
        else:
          right = mid - 1
      elif nums[mid] > nums[right]:
        # in this case, the left must be sorted
        if nums[left] <= target < nums[mid]:
          right = mid - 1
        else:
          left = mid + 1
      else: 
        # the unique situation, we cannot determine which side is mono
        # but we can narrow right index to the left 
        right -= 1 

    return False


## Run code after defining input and solver
input1 = [2,5,6,0,0,1,2]
input2 = 3
solver = Solution().search
print(solver(input1, input2))