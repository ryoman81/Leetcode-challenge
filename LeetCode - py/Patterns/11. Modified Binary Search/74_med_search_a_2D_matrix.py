'''
Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
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
    1. 
  Complexity:
    Time: O()
    Space: O()
  '''
  def searchMatrix(self, matrix, target):
    m = len(matrix)
    n = len(matrix[0])

    up, down, left, right = 0, m-1, 0, n-1

    while up <= down:
      center = (up + down) // 2
      if matrix[center][0] == target:
        return True
      elif matrix[center][0] < target:
        up = center + 1
      else:
        down = center - 1

    up -= 1

    while left <= right:
      mid = (left + right) // 2
      if matrix[up][mid] == target:
        return True
      elif matrix[up][mid] < target:
        left = mid + 1
      else:
        right = mid - 1
      
    return False


## Run code after defining input and solver
input1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
input2 = 7
solver = Solution().searchMatrix
print(solver(input1, input2))