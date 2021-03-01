'''
You are given the root of a binary tree containing digits from 0 to 9 only.
Each root-to-leaf path in the tree represents a number.
For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers.
A leaf node is a node with no children.

Example 1:
Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:
Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
 
Constraints:
The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 9
The depth of the tree will not exceed 10.
'''

# Import helper class TeeNode in this folder
# It is the same as LeetCode one with additional methods show() and create()
from TreeNode import TreeNode

class Solution:
  '''
  MY CODE VERSION
  Thought:
    Exactly the same thought as 129. Use a 'path' to record the current path
    Write a helper function to create the number from current root-to-leaf path
  Complexity:
    Time: O(n) for visiting of each node
    Space: O(H) H is the height of the tree. expense for recursion stack. average O(logn)
  '''
  
  def sumNumbers(self, root):
    path = []
    sumAll = 0
    
    # a closure function
    def DFS (node):
      if not node:
        return
      
      path.append(node.val)
      # if leaf node
      if not node.left and not node.right:
        # be sure to pass a copy of path because path list will be changed
        num = self.converter(path.copy())
        nonlocal sumAll
        sumAll += num
          
      DFS(node.left)
      DFS(node.right)
      path.pop()
    
    DFS(root)
    return sumAll
  
  # A helper method for converting array to required string format
  def converter(self, arr):
    base = 1
    num = 0
    while arr:
      num += arr.pop() * base
      base *= 10
    return num


## Run code after defining input and solver
input1 = TreeNode().create([1,2,3])
solver = Solution().sumNumbers
print(solver(input1))