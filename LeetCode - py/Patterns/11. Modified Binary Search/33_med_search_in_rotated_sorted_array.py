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
    Something learned in this FIRST question
      - when doing conditioning withing while loop, choosing left or right boundary is tricky
        which comparing sign to use? < <= > >=?
      - based on the strategy:
        a) mid may overlap with left
        b) stick on left close and right close template in the most case
  Thought:
    1. there must be one sorted portion in left-mid or mid-right
    2. compare mid with left (因为我是左撇子) using <=, because mid may overlap with left
    3. put target in this region and check if within, then norrow a half of interval
  Complexity:
    Time: O(logn)
    Space: O(1)
  '''

  def search(self, nums, target):
    left = 0
    right = len(nums) - 1

    while (left <= right):
      mid = left + (right - left) // 2
      if (nums[mid] == target): 
        return mid

      # the right is sorted. you can also compare with left
      # but if comparing with left, be sure to use <= since mid may duplicate with left
      if (nums[mid] < nums[right]):
        # target must not be at mid, but it may be at right so use <= at right portion
        if nums[mid] < target <= nums[right]:
          left = mid + 1
        else:
          right = mid - 1
      # else the left is sorted
      else:
        if (nums[left] <= target < nums[mid]):
          right = mid - 1
        else:
          left = mid + 1

    return -1


## Run code after defining input and solver
input1 = [4,5,6,7,8,9,10,11,0,1,2,3]
input2 = 3.3
solver = Solution().search
print(solver(input1, input2))