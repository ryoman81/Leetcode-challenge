'''
QUESTION DESCRIPTION (copy from LeetCode)
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
    Very tricky on the indexing!!!!
    Similar to 33
    I have to remove equal sign in while loop 
    TO BE SUMMARIZE
  Complexity:
    Time: O()
    Space: O()
  '''
  def findMin(self, nums):
    left = 0
    right = len(nums) - 1

    while left < right:
      mid = (left + right) // 2

      # the left part is sorted
      # the minimum could only be on the right
      if nums[mid] > nums[right]:
        left = mid + 1
      else:
        right = mid

    return nums[right]


## Run code after defining input and solver
input = [3,1,2]
solver = Solution().findMin
print(solver(input))