'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?

Example:
Input: [4,3,2,7,8,2,3,1]
Output: [2,3]
'''


class Solution:
  '''
  OPTIMAL CODE VERSION
  Improvement:
    There is no need to update or return result during cyclic sorting stage (like 287)
    We can still stick on the template pattern that
      - sorting firstly
      - check afterwards
  Complexity:
    Time: O(n)
    Space: O(1)
  '''
  def findDuplicatesOpt(self, nums):
    i = 0
    result = []
    # Cyclic sorting stage
    while i < len(nums):
      crr = nums[i]
      # swap to the correct position if possible
      if crr != nums[crr-1]:
        nums[i], nums[crr-1] = nums[crr-1], nums[i]
      else:
        i += 1
    # value checking stage
    for i in range(len(nums)):
      if i != nums[i] - 1:
        result.append(nums[i])
        
    return result

  '''
  MY CODE VERSION
  Thought:
    Similar to 287 and 448, but in this problem, there might be numbers dissappeared or duplicated 
  Complexity:
    Time: O(n)
    Space: O(1)
  '''
  def findDuplicates(self, nums):
    i = 0
    result = []
    while i < len(nums):
      crr = nums[i]
      # swap to the correct position if possible
      if crr != nums[crr-1]:
        nums[i], nums[crr-1] = nums[crr-1], nums[i]
      # else crr is the same as value at [crr-1]
      else:
        # if i not in the postion of [crr-1], it is a duplicate
        # if we have put this duplicate in the result array then we skip it
        if (i != crr-1) and (crr not in result):
          result.append(crr)
        i += 1
        
    return result


## Run code after defining input and solver
input = [4,3,2,7,8,2,3,1]
solver = Solution().findDuplicatesOpt
print(solver(input))