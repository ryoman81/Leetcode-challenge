'''
Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.

Example 1:
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])

Example 2:
Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
 
Note:
The number of nodes in the given list will be between 1 and 100.
'''

# Import helper class ListNode in this folder
# It is the same as LeetCode one with additional methods show() and create()
from ListNode import ListNode

class Solution:
  '''
  MY CODE VERSION
  Thought:
    advance: 0
    speed ratio: 2
  Complexity:
    Time: O(n)
    Space: O(1)
  '''
  def middleNode(self, head):
    fast = head
    slow = head

    while fast.next:
      if fast.next.next == None:
        # the total number is even and fast point is hitting the tail
        return slow.next
      
      fast = fast.next.next
      slow = slow.next

    # if out the while-loop, the total number is odd
    return slow


## Run code after defining input and solver
input = ListNode().create([1])
solver = Solution().middleNode
print(solver(input).show())