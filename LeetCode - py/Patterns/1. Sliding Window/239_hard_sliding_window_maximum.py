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


class monotonicQueue:
  # Initialize a queue structure using List
  def __init__(self):
    self.queue = []
  # Show the max item in queue
  def max(self):
    if len(self.queue) == 0:
      return 0
    return self.queue[0]
  # Pop the first item
  def pop(self):
    if len(self.queue) == 0:
      return
    self.queue.pop(0)
  # Push new item to the end after removing smaller items
  def push(self, item):
    while len(self.queue) != 0 and self.queue[-1] < item:
      self.queue.pop(-1)
    self.queue.append(item)


class Solution:
  '''
  THE OPTIMAL CODE VERSION
  Improvement:
    A smart solution using a monotonic queue
  Thought:
    - maintain a monotonic queue from sliding window
    - special is pushing a new item will remove all other items in the current queue who are larger than it
    - the first element in mono queue is the max in the sliding window
  Complexity:
    Time: O(n)
    Space: O(k)
  '''
  def maxSlidingWindowOpt(self, nums, k: int):
    result = []
    # use mono queue data structure
    mq = monotonicQueue()
    for i in range(len(nums)):
      mq.push(nums[i])
      if i - k + 1 >= 0:
        # if window size is appoached then start to get the max from mono queue
        result.append(mq.max())
        # if the left item of sliding window is the same as the max in mono queue
        # which denotes that the max window size meet in mono queue
        if nums[i-k+1] == mq.max():
          # then we will remove this item from mono queue to meet the window size
          mq.pop()
    # return result
    return result
  '''

  MY CODE VERSION
  Thought:
    This is a brute force solution
    - Use a sliding window and ask for the max number inside the window
    - The answer excess the time limit in LeetCode
  Complexity:
    Time: O(n^2)
    Space: O(k)
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


## Run code after defining input and solver
input1 = [1,3,-1,-3,5,3,6,7]
input2 = 3
solver = Solution().maxSlidingWindowOpt
print(solver(input1, input2))