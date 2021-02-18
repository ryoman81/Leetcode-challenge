'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    A standard BFS traversal by layers. Compared to 102:
      - We create the final result array from bottom to up
  Complexity:
    Time: O(n)
    Space: O(n)
  '''
  def levelOrder(self, root):
    if not root: 
      return None
    
    queue = [root]
    result = []
    
    while queue:
      crrLevel = []
      crrLevelSize = len(queue)
      
      for i in range(crrLevelSize):
        node = queue.pop(0)
        crrLevel.append(node.val)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
              
      result.insert(0, crrLevel)  # put the current layer to the front of the result array
        
    return result


## Since we don't have tree class and a tree creating method
## We don't do test in local environment. Please use LeetCode editor for testing