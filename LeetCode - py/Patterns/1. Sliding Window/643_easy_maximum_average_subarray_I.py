'''
Given an array consisting of n integers, find the contiguous subarray of given length k that 
has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

Constraints:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    1. 
  Complexity:
    Time: O(n)
    Space: O(k)
  '''
  def findMaxAverage(self, nums, k):
    queue = nums[:k]
    result = sum(queue)
    lastSum = result
    
    for i in range(k, len(nums)):
        crrMax = lastSum - queue[0] + nums[i] 
        if (crrMax > result):
            result = crrMax

        lastSum = crrMax
        queue.append(nums[i])
        queue.pop(0)
        
    return result/k


## Run code after defining input and solver
input1 = [1,12,-5,-6,50,3]
input2 = 4
solver = Solution().findMaxAverage
print(solver(input1, input2))