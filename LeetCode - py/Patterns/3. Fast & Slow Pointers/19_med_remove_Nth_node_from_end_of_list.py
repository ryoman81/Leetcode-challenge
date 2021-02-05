'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Follow up: Could you do this in one pass?

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
 
Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
'''

# Import helper class ListNode in this folder
# It is the same as LeetCode one with additional methods show() and create()
from ListNode import ListNode

class Solution:
  '''
  MY CODE VERSION
  Thought:
    advance: n
    speed ratio: 1
  Complexity:
    Time: O(n)
    Space: O(1)
  '''
  def removeNthFromEnd(self, head, n):
    fast = head
    slow = head

    # define distance and moving speed of fast and slow pointers
    # for this problem, moving speed are the same, fast head of slow by n
    for i in range(n):
      fast = fast.next
    
    # boundary that n equals to the length of list, which means remove the head element
    if fast == None:
      return head.next
 
    # loop until fast meet tail
    while fast.next:
      fast = fast.next
      slow = slow.next
    
    slow.next = slow.next.next

    return head


## Run code after defining input and solver
input1 = ListNode().create([1])
input2 = 1
solver = Solution().removeNthFromEnd
print(solver(input1, input2).show())