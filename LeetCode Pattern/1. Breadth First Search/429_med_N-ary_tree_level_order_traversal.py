'''
Given an n-ary tree, return the level order traversal of its nodes' values.
Nary-Tree input serialization is represented in their level order traversal,
each group of children is separated by the null value (See examples).

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
 
Constraints:
The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 104]
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    A standard BFS traversal by layers. Compared to 102:
      - A node may have multiple children rather than left and right
      - We loop over all child at a single node
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
        # loop over all children rather than left and right
        for kid in node.children:
          queue.append(kid)
      
      result.append(crrLevel)
    
    return result


## Since we don't have tree class and a tree creating method
## We don't do test in local environment. Please use LeetCode editor for testing