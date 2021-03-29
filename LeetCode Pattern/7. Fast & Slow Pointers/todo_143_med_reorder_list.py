'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:
Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''


# Import helper class ListNode in this folder
# It is the same as LeetCode one with additional methods show() and create()
from ListNode import ListNode

class Solution:
  '''
  MY CODE VERSION
  Thought:
    
  Complexity:
    Time: O()
    Space: O()
  '''
  def reorderList(self, head):
    """
    Do not return anything, modify head in-place instead.
    """
    if not head:
      return None

    # find the middle point    
    slow = head
    fast = head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next
      fast = fast.next

    # reverse the second half part of list
    second = self.reverse(slow)

    # combine first and second half of the list
    first = head
    while second.next:
      temp = first.next
      first.next = second
      first = temp

      temp = second.next
      second.next = first
      second = temp

    return head

  # HELPER FUNCTION TO REVERSE LIST
  def reverse(self, head):
    left = None
    middle = head
    while middle:
      right = middle.next
      middle.next = left
      left = middle
      middle = right
    return left

## Run code after defining input and solver
input1 = ListNode().create([1,2,3,4,5,6])
solver = Solution().reorderList
print(solver(input1).show())