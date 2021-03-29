'''
Remove all elements from a linked list of integers that have value val.

Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''

# Import helper class ListNode in this folder
# It is the same as LeetCode one with additional methods show() and create()
from ListNode import ListNode

class Solution:
  '''
  MY CODE VERSION
  Thought:
    Actually this is not too much of slow & fast pointer pattern
    We can do slow fast pointers by advancing fast by 1 and move in same speed
    Or just use crr.next.next to represent fast.next
  Complexity:
    Time: O(n)
    Space: O(1)
  '''
  def removeElements(self, head, val):
    # remove target value in head position
    while head != None and head.val == val:
      head = head.next
    
    # error check if head is now empty
    if head == None:
      return head

    crr = head
    while crr.next:
      # if next value is target, move pointer to the one after
      if crr.next.val == val:
        crr.next = crr.next.next
      # otherwise advance pointer 
      else:
        crr = crr.next

    return head


## Run code after defining input and solver
input1 = ListNode().create([6,6,5,4,1,3,9])
input2 = 6
solver = Solution().removeElements
print(solver(input1, input2).show())