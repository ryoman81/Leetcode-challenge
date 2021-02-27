'''
Given two integer arrays inorder and postorder where inorder is the inorder traversal of 
a binary tree and postorder is the postorder traversal of the same tree, 
construct and return the binary tree. 

Example 1:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: inorder = [-1], postorder = [-1]
Output: []
 
Constraints:
1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
'''

# Import helper class TeeNode in this folder
# It is the same as LeetCode one with additional methods show() and create()
from TreeNode import TreeNode

class Solution:
  '''
  OPTIMAL VERSION
  Thought:
    
  Complexity:
    Time: O(n)
    Space: O()
  '''
  def buildTree(self, inorder, postorder):
    def DFS (in_start, in_end, post_start, post_end):
      if post_start > post_end:
        return None
      if post_start == post_end:
        return TreeNode(postorder[post_start])
      
      node = TreeNode(postorder[post_end])
      i = inorder.index(postorder[post_end])

      # the index of new end for postorder array
      newEnd = post_start + ((i-1) - in_start)

      node.left = DFS(in_start, i-1, post_start, newEnd)
      node.right = DFS(i+1, in_end, newEnd+1, post_end-1)

      return node

    return DFS(0, len(inorder)-1, 0, len(postorder)-1)

  '''
  SIMPLIFIED VERSION
  Thought:
    
  Complexity:
    Time: O(n)
    Space: O()
  '''
  def buildTree2(self, inorder, postorder):
    # base case if the input array is empty
    if not postorder:
      return None

    # the last item of postorder must be the root
    node = TreeNode(postorder[-1])
    # find the index of root in inorder array
    i = inorder.index(postorder[-1])

    # For inorder array, [0:i] is the left part of current node, [i+1:] is the right part
    # For postorder array, [1:i+1] is the left part of current node, [i+1:] is the right part
    node.left = self.buildTree(inorder[0:i], postorder[0:i])
    node.right = self.buildTree(inorder[i+1:], postorder[i:-1])
    
    return node


## Run code after defining input and solver
input1 = [9,3,15,20,7]
input2 = [9,15,7,20,3]
solver = Solution().buildTree
print(solver(input1, input2).show())