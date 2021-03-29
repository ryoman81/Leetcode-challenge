'''
Given an integer array nums where the elements are sorted in ascending order, 
convert it to a height-balanced binary search tree.
A height-balanced binary tree is a binary tree in which the depth of the 
two subtrees of every node never differs by more than one.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,3] and [3,1] are both a height-balanced BSTs.
 
Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
'''

# Import helper class TeeNode in this folder
# It is the same as LeetCode one with additional methods show() and create()
from TreeNode import TreeNode

class Solution:
  '''
  OPTIMAL VERSION
  Thought:
    Please see the belowing simplified answer first
    This is an optimization with the same idea of 105, 106, 889 
    that use closure and avoid copying new array
  Complexity:
    Time: O(n)
    Space: O(H)
  '''
  def sortedArrayToBST(self, nums):
    def DFS (start, end):
      if start > end: 
        return None
      if start == end:
        return TreeNode(nums[start])
      
      mid = (start + end) // 2
      node = TreeNode(nums[mid])
      node.left = DFS(start, mid-1)
      node.right = DFS(mid+1, end)

      return node
    
    return DFS(0, len(nums)-1)

  '''
  SIMPLIFIED VERSION
  Thought:
    The problem is very typical that construct BST from sorted array
    Follow the principle that
      - The middle point of current array is the root to be reconstructed
      - left part of middle are left children
      - right part of middle are right children
      - recursion to create until no more items in array
    A brilliant solution is to reconstruct via in-order traversal. Please see 109 
  Complexity:
    Time: O(n)
    Space: O(H) without considering copying array
  '''
  def sortedArrayToBST1(self, nums):
    if not nums: 
      return None
    
    left = 0
    right = len(nums) - 1
    
    mid = (left + right) // 2
    
    node = TreeNode(nums[mid])
    node.left = self.sortedArrayToBST(nums[0:mid])
    node.right = self.sortedArrayToBST(nums[mid+1:])
    
    return node

## Run code after defining input and solver
input1 = [-10,-3,0,5,9]
solver = Solution().sortedArrayToBST
print(solver(input1).show())