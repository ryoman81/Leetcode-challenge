'''
Find the kth largest element in an unsorted array. 
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''

# Import helper class maxHeap in this folder
from Heap import maxHeap


class Solution:
  '''
  THE OPTIMAL CODE VERSION
  Improvement:
    Of course you cannot use a third-party module or library
    Even Java and C++ provide internal data structure of priority queue (binary heap) that you can use
    But the interviewer won't like you to do that like the belowing answer
    Let's do it within the solution
  Thought:
    Heap: no library introduced
      - Heapify the input array to a max-heap  // O(n)
      - Extract top (the maximum) k-1 times    // O(klogn) 
  Complexity:
    Time: O(klogn + n)
    Space: O(1)
  '''
  def findKthLargest(self, nums, k):
    # we will create a closure function siftDown for heapifying and extracting methods
    def siftDown (arr, current):
      # find the index of left and right children
      left = current * 2 + 1
      right = current * 2 + 2
      # loop over to sift down this item
      while left < len(arr):
        # find the max child to be swapped
        maxChild = left
        # check if right is larger than the left
        if right < len(arr) and arr[right] > arr[left]:
          maxChild = right
        # doing a swap to sift down the current 
        if arr[current] < arr[maxChild]:
          arr[current], arr[maxChild] = arr[maxChild], arr[current]
        else:
          return
        # update index
        current = maxChild
        left = current * 2 + 1
        right = left + 1     

    # the first step is to heapify the nums array we will do it in-place of the list
    i = len(nums) // 2
    while i >= 0:
      siftDown(nums, i)
      i -= 1

    # then we will extract (pop) the top of nums for k-1 times
    max = 0
    for i in range(0, k):
      max = nums[0]   # record the current max value
      nums[0], nums[-1] = nums[-1], nums[0]   # swap top and tail of heap list
      nums.pop()    # pop out the last item
      siftDown(nums, 0)     # sift down the top item to maintain the heap structure

    # return the final result
    return max

  '''
  MY CODE VERSION
  Thought:
    Heap: using my own maxHeap class
      - Heapify the input array to a max-heap  // O(n)
      - Extract top (the maximum) k-1 times    // O(klogn)
  Complexity:
    Time: O(klogn + n)
    Space: O(n)
  '''
  def findKthLargest1(self, nums, k):
    # heapify the nums array
    heap = maxHeap()
    heap.heapify(nums)

    kthMax = nums[0]
    # extract (pop) the top for k-1 times
    for i in range(0, k):
      kthMax = heap.extract()

    return kthMax

  '''
  SIMPLE CODE VERSION
  Thought:
    Silly solution, very easy
      - Sort the input array reversely
      - return the k-1th element
  Complexity:
    Time: O(nlogn)
    Space: O(1)
  '''
  def findKthLargest2(self, nums, k):
    nums.sort(reverse=True)
    return nums[k-1]


## Run code after defining input and solver
input1 = [3,2,3,1,2,4,5,5,6]
input2 = 4
solver = Solution().findKthLargest
print(solver(input1, input2))