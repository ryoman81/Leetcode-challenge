'''
Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# Import helper class ListNode in this folder
# It is the same as LeetCode one with additional methods show() and create()
from ListNode import ListNode

class Solution:
  '''
  MY CODE VERSION
  Thought:
    - Reversal of linked list is all about change 'next' pointer
    - At each iteration:
      1. determine the left, middle, and right pointers
      2. change middle.next to the left
      3. move left to the middle
      4. move middle to the right
    - At the end after while-loop, change the original head pointing to null
    - Return left because left has moved to the end of original list and now becomes the head of reversed list
  Complexity:
    Time: O(n)
    Space: O(1)
  '''
  def reverseList(self, head):
    if head == None or head.next == None:
      return head

    left = head
    middle = head.next
    while middle:
      right = middle.next
      middle.next = left
      left = middle
      middle = right

    head.next = None
    return left


## Run code after defining input and solver
input = ListNode().create([1,2,5,6,8])
solver = Solution().reverseList
print(solver(input).show())