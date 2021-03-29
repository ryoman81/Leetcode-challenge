'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    A standard BFS traversal by layers. Compared to 102:
      - Use an additional variable isFromLeft to determine the order in current layer
  Complexity:
    Time: O(n)
    Space: O(n)
  '''
  def levelOrder(self, root):
    if not root: 
      return None
    
    queue = [root]
    result = []
    isFromLeft = True
    
    while queue:
      crrLevel = []
      crrLevelSize = len(queue)
      
      for i in range(crrLevelSize):
        node = queue.pop(0)
        if isFromLeft:
          crrLevel.append(node.val)     # create crrLevel from left to right
        else:
          crrLevel.insert(0, node.val)  # create crrLevel from right to left

        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
              
      result.append(crrLevel)
      isFromLeft = not isFromLeft       # toggle isFromLeft for next layer
        
    return result


## Since we don't have tree class and a tree creating method
## We don't do test in local environment. Please use LeetCode editor for testing