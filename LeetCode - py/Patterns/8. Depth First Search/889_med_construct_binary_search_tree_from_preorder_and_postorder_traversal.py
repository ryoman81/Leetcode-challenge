'''
Return any binary tree that matches the given preorder and postorder traversals.
Values in the traversals pre and post are distinct positive integers.

Example 1:
Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
 
Note:
1 <= pre.length == post.length <= 30
pre[] and post[] are both permutations of 1, 2, ..., pre.length.
It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.
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
  def buildTree(self, preorder, postorder):
    # base case if the input array is empty
    if not preorder:
      return None

    # the first item of preorder must be the root
    node = TreeNode(preorder[0])
    # the second item (if exist) of preorder must be on left
    if len(preorder) == 1: return node
    # find this index in postorder array
    i = postorder.index(preorder[1])

    # For preorder array, [1:i+2] is the left part of current node, [i+2:] is the right part
    # For postorder array, [0:i+1] is the left part of current node, [i+1:-1] is the right part
    node.left = self.buildTree(preorder[1:i+2], postorder[0:i+1])
    node.right = self.buildTree(preorder[i+2:], postorder[i+1:-1])
    
    return node


## Run code after defining input and solver
input1 = [1,2,4,5,3,6,7]
input2 = [4,5,2,6,7,3,1]
solver = Solution().buildTree
print(solver(input1, input2).show())