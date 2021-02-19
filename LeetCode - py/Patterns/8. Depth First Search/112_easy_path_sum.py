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


class Solution:
  '''
  MY CODE VERSION
  Thought:
    
  Complexity:
    Time: O(n)
    Space: O()
  '''
  
  def hasPathSum(self, root, targetSum):
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

## Since we don't have tree class and a tree creating method
## We don't do test in local environment. Please use LeetCode editor for testing