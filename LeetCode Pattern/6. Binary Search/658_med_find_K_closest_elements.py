'''
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. 
The result should also be sorted in ascending order.
An integer a is closer to x than an integer b if:
|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 
Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
 
Constraints:
1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
'''


class Solution:
  '''
  THE OPTIMAL CODE VERSION
  Improvement:
    Think the output window should be [left, left+k), which is left closure and right open form
    Here we should better use the other form of template that
      1. left = 0, right = len(arr), then shift right by k and becomes right = len(arr) - k
      2. while-loop condition goes without equal sign that left < right
  Thought:
    1.  
  Complexity:
    Time: O(logn)
    Space: O(1)
  '''
  def findClosestElements(self, arr, k, x):
    left = 0
    right = len(arr) - k

    while left < right:
      mid = (left + right) // 2
      if x - arr[mid] > arr[mid+k] -x:
        left = mid + 1
      else:
        right = mid

    return arr[left:left+k]


## Run code after defining input and solver
input1 = [1,2,3,4,5]
input2 = 2
input3 = 5
solver = Solution().findClosestElements
print(solver(input1,input2,input3))