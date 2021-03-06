'''
Given a collection of numbers, nums, that might contain duplicates, 
return all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 
Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    1. 
  Complexity:
    Time: O()
    Space: O()
  '''
  def permuteUnique(self, nums):
    # sort nums list hence we can find duplicate easily
    nums.sort()

    result = []
    path = []
    used = [False] * len(nums)

    def backtracking ():
      if len(path) == len(nums):
        result.append(path[:])
        return
      
      for i in range(len(nums)):
        # pruning step
        if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
          continue
        path.append(nums[i])
        used[i] = True
        backtracking()
        path.pop()
        used[i] = False

    backtracking()

    return result


## Run code after defining input and solver
input = [1,1,1,1,2]
solver = Solution().permuteUnique
print(solver(input))