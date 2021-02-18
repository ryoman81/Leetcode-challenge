'''
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest 
path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

Constraints:
The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    This is a standard question of BFS in a binary tree. Follow template should be good
      - We use a variable 'depth' to count the number of layers we have been through
      - Return the depth once a node has no left or right child
  Complexity:
    Time: O(n)
    Space: O(1); worst O(n) if height=numNodes
  '''
  def minDepth(self, root: TreeNode) -> int:
    if not root:
      return 0
    
    queue = [root]
    depth = 0
    
    while queue:
      depth += 1
      levelSize = len(queue)
      for i in range(levelSize):
        node = queue.pop(0)

        if not node.left and not node.right:
          return depth

        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
    
    return depth


## Since we don't have tree class and a tree creating method
## We don't do test in local environment. Please use LeetCode editor for testing