'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal 
of a binary tree and inorder is the inorder traversal of the same tree, 
construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints:
1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
'''

# Import helper class TeeNode in this folder
# It is the same as LeetCode one with additional methods show() and create()
from TreeNode import TreeNode

class Solution:
  '''
  OPTIMAL CODE VERSION
  Thought:
    
  Complexity:
    Time: O(n)
    Space: O()
  '''
  def buildTree(self, preorder, inorder):

    def DFS (pre_start, pre_end, in_start, in_end):
      if pre_start > pre_end: 
        return None
      if pre_start == pre_end:
        return TreeNode(preorder[pre_start])
      
      node = TreeNode(preorder[pre_start])
      i = inorder.index(preorder[pre_start])

      # calculate new end in preorder array
      newEnd = pre_start + 1 + ((i-1) - in_start)

      node.left = DFS (pre_start+1, newEnd, in_start, i-1)
      node.right = DFS (newEnd+1, pre_end, i+1, in_end)

      return node
    
    return DFS (0, len(preorder)-1, 0, len(inorder)-1)

  '''
  SIMPLIFIED VERSION
  Thought:
    
  Complexity:
    Time: O(n)
    Space: O()
  '''
  def buildTree2(self, preorder, inorder):
    # base case if the input array is empty
    if not preorder:
      return None

    # the first item of preorder must be the root
    node = TreeNode(preorder[0])
    # find the index of root in inorder array
    i = inorder.index(preorder[0])

    # For inorder array, [0:i] is the left part of current node, [i+1:] is the right part
    # For preorder array, [1:i+1] is the left part of current node, [i+1:] is the right part
    node.left = self.buildTree(preorder[1:i+1], inorder[0:i])
    node.right = self.buildTree(preorder[i+1:], inorder[i+1:])
    
    return node


## Run code after defining input and solver
input1 = [3,9,20,15,7]
input2 = [9,3,15,20,7]
solver = Solution().buildTree
print(solver(input1, input2).show())