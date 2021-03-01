'''
You are given a binary tree in which each node contains an integer value.
Find the number of paths that sum to a given value.
The path does not need to start or end at the root or a leaf, 
but it must go downwards (traveling only from parent nodes to child nodes).
The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:
1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
'''

# Import helper class TeeNode in this folder
# It is the same as LeetCode one with additional methods show() and create()
from TreeNode import TreeNode

class Solution:
  '''
  MY CODE VERSION
  Thought:
    The question is very similar to the stock sell-buy problems of DP. 
      The key is to maintain a data structure to record the "previous sum"
      We make decision from this cumulated sum
    The required path is not limited to root-to-leaf but still top-to-down, hence,
      1. we use a closure variable to record the current cumulated sum at this point
      2. we calculate the distance between this cumulatedSum and target
      3. if there exist a value in the path link, which means:
          there exists a result in this path link
          take a look at animation online 

    This solution is not optimal. The data structure we use is an array/list
      Searching in a list is not efficient
      A hash table is more desired
  Complexity:
    Time: O(n)    # may not accurate
    Space: O(H)   # may not accurate
  '''
  
  def pathSum(self, root, targetSum):
    result = 0
    # since it is the stack of path to record the cumulated sum
    # we should push in 0 at the bottom (think why?: because the initial sum is 0 -_-)
    path = [0]

    def DFS(node, cumulatedSum):
      # base case
      if not node:
        return
      
      # calculate the current cumulated sum value
      crrCumSum = cumulatedSum + node.val
      # find the diff between target and current cumulated sum
      diff = crrCumSum - targetSum
      # search if diff exists in the path of cumulated sum
      for item in path:
        if item == diff: 
          nonlocal result
          result += 1
      
      # recursion
      path.append(crrCumSum)
      DFS(node.left, crrCumSum)
      DFS(node.right, crrCumSum)
      path.pop()

    DFS(root, 0)
    return result


## Run code after defining input and solver
input1 = TreeNode().create([5,4,8,11,None,13,4,7,2,None,None,5,1])
input2 = 22
solver = Solution().pathSum
print(solver(input1, input2))