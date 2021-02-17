'''
Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    1. 
  Complexity:
    Time: O()
    Space: O()
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
              
      result.append(crrLevel)
        
    return result


## Run code after defining input and solver
input = ''
solver = Solution().function
print(solver(input))