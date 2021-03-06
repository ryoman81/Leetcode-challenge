'''
Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the nodes of the first two lists.

Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: l1 = [], l2 = []
Output: []

Example 3:
Input: l1 = [], l2 = [0]
Output: [0]
 
Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
'''

# Import helper class ListNode in this folder
# It is the same as LeetCode one with additional methods show() and create()
from ListNode import ListNode

class Solution:
  '''
  MY CODE VERSION
  Thought:
    1. Loop over l1 and l2 before one of them comes to the end
    2. Append the smaller value to the current list
    3. March forward pointers after each comparison
    4. When finished, append the remaining part of l1 or l2 to the current list
  Complexity:
    Time: O(m+n)
    Space: O(1)
  '''
  def function(self, l1, l2):
    head = ListNode()
    crr = head
    # loop over l1 and l2 before the end of each one
    while l1 and l2:
      if l1.val < l2.val:
        crr.next = ListNode(l1.val)
        crr = crr.next
        l1 = l1.next
      else:
        crr.next = ListNode(l2.val)
        crr = crr.next
        l2 = l2.next
    
    # check if any remaining part of l1 or l2
    # We don't need to loop over l1 or l2
    # just use crr.next to point to the remaining part of l1 or l2
    if l1:
      crr.next = l1
    if l2:
      crr.next = l2
    # return head.next because the head was initialized with value 0
    # the true start of this list from the next point
    return head.next


## Run code after defining input and solver
input1 = ListNode().create([1,2,6,8])
input2 = ListNode().create([0,3])
solver = Solution().function
print(solver(input1, input2).show())