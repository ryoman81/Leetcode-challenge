'''
You are given an array of integers nums, there is a sliding window of size k
which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. 
Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1,-1], k = 1
Output: [1,-1]
 
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
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
    def maxSlidingWindow(self, nums, k):
      queue = nums[:k]
      right = k
      result = []
      while right < len(nums):
        result.append(max(queue))
        queue.append(nums[right])
        queue.pop(0)
        right += 1
      result.append(max(queue))

      return result

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
    def maxSlidingWindowOpt(self, nums, k: int):
      return 0


## Run code after defining input and solver
input1 = [1,3,-1,-3,5,3,6,7]
input2 = 3
solver = Solution().maxSlidingWindow
print(solver(input1, input2))