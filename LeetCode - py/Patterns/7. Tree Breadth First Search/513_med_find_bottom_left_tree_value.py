'''
Given the root of a binary tree, return the leftmost value in the last row of the tree.

Example 1:
Input: root = [2,1,3]
Output: 1

Example 2:
Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7
 
Constraints:
The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    A standard BFS traversal by layers.
      - Use a variable leftMost to record the left most node value
  Complexity:
    Time: O(n)
    Space: O(1); worst O(n) if height=numNodes
  '''
  def findBottomLeftValue(self, root):
    if not root:
      return None
    
    queue = [root]
    
    while queue:
      levelSize = len(queue)
      leftMost = queue[0].val   # record left most node value in current layer
      for i in range(levelSize):
        node = queue.pop(0)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
                
    return leftMost


## Since we don't have tree class and a tree creating method
## We don't do test in local environment. Please use LeetCode editor for testing