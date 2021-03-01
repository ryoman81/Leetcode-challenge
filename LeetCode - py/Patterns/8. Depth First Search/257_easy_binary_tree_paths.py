'''
Given a binary tree, return all root-to-leaf paths.
Note: A leaf is a node with no children.

Example:
Input:

   1
 /   \
2     3
 \
  5
Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''

# Import helper class TeeNode in this folder
# It is the same as LeetCode one with additional methods show() and create()
from TreeNode import TreeNode

class Solution:
  '''
  MY CODE VERSION
  Thought:
    Same thought as 113. Use a 'path' to record the current path
    Write a helper function to create a required string '1->2->3'
  Complexity:
    Time: O(n) for visiting of each node
    Space: O(H) H is the height of the tree. expense for recursion stack. average O(logn) 
  '''
  
  def binaryTreePaths(self, root):
    result = []
    path = []
    
    # a closure function
    def DFS (node):
      if not node:
        return
      
      path.append(node.val)
      # if leaf node
      if not node.left and not node.right:
        string = self.stringfy(path)
        result.append(string)
          
      DFS(node.left)
      DFS(node.right)
      path.pop()
    
    DFS(root)
    return result
  
  # A helper method for converting array to required string format
  def stringfy(self, arr):
    string = str(arr[0])
    for i in range(1, len(arr)):
      string = string + '->' + str(arr[i])
    return string


## Run code after defining input and solver
input1 = TreeNode().create([1,2,3,None,5])
solver = Solution().binaryTreePaths
print(solver(input1))