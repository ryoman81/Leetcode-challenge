'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 
Constraints:
The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
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
  
  def maxPathSum(self, root):
    result = float('-inf')

    def DFS(node):
      # base case
      if not node:
        return 0
      
      # recursion: each node returns its max gain at this point
      left_gain = max(0, DFS(node.left))
      right_gain = max(0, DFS(node.right))

      # current gain
      crr_gain = left_gain + right_gain + node.val

      # update result if current gain is globally max
      nonlocal result
      result = max(result, crr_gain)

      return max(left_gain, right_gain) + node.val

    DFS(root)
    return result


## Run code after defining input and solver
input1 = TreeNode().create([-10,9,20,None,None,15,7])
solver = Solution().maxPathSum
print(solver(input1))