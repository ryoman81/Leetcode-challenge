'''
Given an array nums, write a function to move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

class Solution:
  '''
  OPTIMAL CODE VERSION
  Thought:
    Definitely a two pointer problem like 27
    The different point is it requires to maintain the original order
    So, we should not use left and right pointers, but a fast and slow pointers
  Complexity:
    Time: O(n)
    Space: O(1)
  '''
  def moveZeroes(self, nums):
    slow = 0
    fast = 0

    while fast < len(nums):
      if nums[fast] != 0:
        nums[slow], nums[fast] = nums[fast], nums[slow]
        slow += 1
      fast += 1


## Run code after defining input and solver
input = [0,1,0,3,12]
solver = Solution().moveZeroes
print(solver(input))