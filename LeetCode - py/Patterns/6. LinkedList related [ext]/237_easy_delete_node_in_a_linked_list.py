'''
Write a function to delete a node in a singly-linked list. 
You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.
It is guaranteed that the node to be deleted is not a tail node in the list.

Example 1:
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

Constraints:
The number of the nodes in the given list is in the range [2, 1000].
-1000 <= Node.val <= 1000
The value of each node in the list is unique.
The node to be deleted is in the list and is not a tail node
'''

class Solution:
  '''
  MY CODE VERSION
  Thought:
    An interesting setting is that we have NO ACCESS to the node before the target
    if we want to remove current node
      - let the current node value becomes the next one's value
      - and make the current node point to the next next one
    WHAT AN INSANE QUESTION!!!! 可以想象跳出思维定式有多重要
  Complexity:
    Time: O(1)
    Space: O(1)
  '''
  def deleteNode(self, node):
    node.val = node.next.val
    node.next = node.next.next
    return


## No need for testing......