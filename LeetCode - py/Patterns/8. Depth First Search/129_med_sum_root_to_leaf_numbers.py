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
    
  Complexity:
    Time: O(n)
    Space: O()
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