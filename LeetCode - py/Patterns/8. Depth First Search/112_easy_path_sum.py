'''
Given the root of a binary tree and an integer targetSum, return true if the tree has 
a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false

Example 3:
Input: root = [1,2], targetSum = 0
Output: false
 
Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
'''

# Import helper class TeeNode in this folder
# It is the same as LeetCode one with additional methods show() and create()
from TreeNode import TreeNode

class Solution:
  '''
  MY CODE VERSION
  Thought:
    Follow template of path traversal
      - maintain a closure varibale ifHasPath
      - 
  Complexity:
    Time: O(n)
    Space: O()
  '''
  def hasPathSum(self, root, targetSum):
    # define the closure variables
    ifHasPath = False
    
    # define the recursion function
    def DFS(node, sum):
      # base case
      if not node:
        return

      # ending condition that the node is leaf
      if not node.left and not node.right:
        if node.val == sum:
          # change closure variable
          ### 这是python和js非常大的不同点, 如果不声明ifHasPath是外层变量, 则无法对其修改
          ### 必须要使用nonlocal关键字指定它定义在closure内
          ### 在JavaScript中则可直接对函数外层定义的ifHasPath进行更新
          nonlocal ifHasPath
          ifHasPath = True

      # recursion step 
      # (this is pre-order because we did something before moving on next left and right)
      DFS(node.left, sum-node.val)
      DFS(node.right, sum-node.val)

    # enter recursion by calling sub function
    DFS(root, targetSum)  
    return ifHasPath

  '''
  SIMPLIFIED CODE VERSION
  Thought:
    This version was shown frequently online. 
    It is simplified without writing an additional sub function.
    If want to follow template, please see my code version
  Complexity:
    Time: O(n)
    Space: O()
  '''
  def hasPathSum2(self, root, targetSum):
    # base case
    if not root:
      return
    
    # check if leaf
    if not root.left and not root.right:
      # check if leaf value is the same as input target
      if root.val == targetSum:
        return True
      else:
        return False
    
    # if not leaf pass target - val to the next node
    return self.hasPathSum(root.left, targetSum-root.val) or\
           self.hasPathSum(root.right, targetSum-root.val)


## Run code after defining input and solver
input1 = TreeNode().create([5,4,8,11,None,13,4,7,2,None,None,None,1])
input2 = 22
solver = Solution().hasPathSum
print(solver(input1, input2))