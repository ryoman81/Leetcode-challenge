'''
Given an n x n matrix where each of the rows and columns are sorted 
in ascending order, return the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5
 
Constraints:
n == matrix.length
n == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= -109
All the rows and columns of matrix are guaranteed to be sorted in non-degreasing order.
1 <= k <= n2
'''


# Import helper class maxHeap in this folder
from Heap import minHeap    # for my code version
import heapq                # for other version

class Solution:
  '''
  OTHER VERSION
  Thought:
    Modification of my code by using official heapq module
  Complexity:
    Time: O(klogn)
    Space: O(n)
  '''
  def kthSmallestOpt(self, matrix, k):
    # flatten the matrix from 2D to 1D  // O(n)
    arr = []
    for row in matrix:
      arr += row
    # heapify the arr to a min heap     // O(n)
    heapq.heapify(arr)
    # pop k time to get the kth smallest item   // O(klogn)
    for i in range(k-1):
      heapq.heappop(arr)
    return heapq.heappop(arr)


  '''
  MY CODE VERSION
  Thought:
    - we need to convert the input matrix to a 1D array (for heap structuring)
    - then we heapify the array, the top item is the smallest
    - we pop k time, the last popped result is the kth smallest
  Complexity:
    Time: O(klogn)
    Space: O(n)
  '''
  def kthSmallest(self, matrix, k):
    # flatten the matrix from 2D to 1D  // O(n)
    arr = []
    for row in matrix:
      arr += row
    # heapify the arr to a min heap     // O(n)
    heap = minHeap()
    heap.heapify(arr)
    # pop k time to get the kth smallest item   // O(klogn)
    for i in range(k-1):
      heap.extract()
    return heap.extract()
    

## Run code after defining input and solver
input1 = [[1,5,9],[10,11,13],[12,13,15]]
input2 = 8
solver = Solution().kthSmallestOpt
print(solver(input1, input2))