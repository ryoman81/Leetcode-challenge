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

    def DFS(node, sum, path):
      # base case
      if not node:
        return
    
      # check if leaf
      if not node.left and not node.right:
        # check if leaf value is the same as input target
        if node.val == sum:
          path.append(node.val)
          result.append(path)
        return
      
      path.append(node.val)
      path_left = path.copy()
      DFS(node.left, sum-node.val, path_left)
      path_right = path.copy()
      DFS(node.right, sum-node.val, path_right)

    DFS(root, targetSum, [])
    return result


## Since we don't have tree class and a tree creating method
## We don't do test in local environment. Please use LeetCode editor for testing