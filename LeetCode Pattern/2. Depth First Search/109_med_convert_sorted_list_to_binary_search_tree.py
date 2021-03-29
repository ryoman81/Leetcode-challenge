'''
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which
the depth of the two subtrees of every node never differ by more than 1.

Example 1:
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
'''

# Import helper class TeeNode in this folder
# It is the same as LeetCode one with additional methods show() and create()
from TreeNode import TreeNode

class Solution:
  '''
  OPTIMAL VERSION
  Thought:
    - The essential idea is that 
        The in-order traversal of a BST will return an ascending sorted array
    - Since here is not an array but a linked list, we cannot use method in 108 to access the middle point
    
    * SIMPLE SOLUTION is convert linked list to an array

    Here is one brilliant solution
      1. first loop over list to get the total length of all nodes
      2. we design a recursion function acccepting the start and end index
        - The recursion follow the in-order traversal pattern
        - Although we don't know what is the value at 'mid' we just do recursion
        - The whole tree will be contructured from the LEFT BOTTOM
        - And it follows the order LEFT -> ROOT -> RIGHT
        - Every time a node is reconstructed, the head is advanced
  Complexity:
    Time: O(n)
    Space: O(H)
  '''
  def sortedListToBST(self, head: ListNode) -> TreeNode:
    # loop over linked list to obtain its length
    size = 0
    p = head
    while p:
      size += 1
      p = p.next
    
    # recursion function    
    def inorderDFS (start, end):
      # base condition
      if start > end:
          return None

      # since we update closure variable head directly, we should claim nonlocal in Python
      nonlocal head

      # find the mid point
      mid = (start + end) // 2
      # create an empty node
      node = TreeNode()

      # the following step is similar to the in-order traversal
      # traversal to the left
      node.left = inorderDFS(start, mid - 1)
      # create current node value (an inverse step of recording current node value)
      node.val = head.val
      # advance head to the next
      head = head.next
      # traversal to the right
      node.right = inorderDFS(mid + 1, end)
      
      return node
    
    return inorderDFS(0, size - 1)

## No test run in this problem