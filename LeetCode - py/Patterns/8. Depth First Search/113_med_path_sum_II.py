'''
Given the root of a binary tree and an integer targetSum, 
return all root-to-leaf paths where each path's sum equals targetSum.
A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:
Input: root = [1,2], targetSum = 0
Output: []
 
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
    
  Complexity:
    Time: O(n)
    Space: O()
  '''
  
  def hasPathSum(self, root, targetSum):
    result = []
    path = []

    def DFS(node, sum):
      # base case
      if not node:
        return
      ### 此处在闭包DFS中也要使用外层函数定义的变量path, 但不需要声明 nonlocal. 
      ### 因为path声明的是数组, 作为数组的引用, 我们并没有直接修改path这个变量.
      path.append(node.val)
      # check if leaf
      if not node.left and not node.right:
        # check if leaf value is the same as input target
        if node.val == sum:
          # KEY: we must append a hard copy of path to the result array, otherwise, path change, result changes
          result.append(path.copy())
      
      DFS(node.left, sum-node.val)
      DFS(node.right, sum-node.val)
      path.pop()

    DFS(root, targetSum)
    return result


## Run code after defining input and solver
input1 = TreeNode().create([5,4,8,11,None,13,4,7,2,None,None,5,1])
input2 = 22
solver = Solution().hasPathSum
print(solver(input1, input2))