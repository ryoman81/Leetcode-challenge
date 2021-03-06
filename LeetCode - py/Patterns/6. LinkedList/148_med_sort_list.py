'''
Given the head of a linked list, return the list after sorting it in ascending order.
Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
'''

# Import helper class ListNode in this folder
# It is the same as LeetCode one with additional methods show() and create()
from ListNode import ListNode

class Solution:
  '''
  MY CODE VERSION
  Thought:
    The basic idea is using merge sort
    The key is to find the mid point of current list
      - first loop over current list to find the length
      - then loop over current list to the mid point
      - break current list by setting right=mid.next and changing mid.next = null
      - then the left half is 'head' and the right half is 'right'
    Do a recursive merge as standard merge sort like: return merge(sort(left), sort(right))
  Complexity:
    Time: O(nlogn)  merge sort
    Space: O(logn)  recursion stack
  '''
  def sortList(self, crrList):
    ## initial error check for empty list
    if not crrList:
      return None

    ## base condition for exiting recursion
    # if the current list is a single node then we should end recursion
    if crrList.next == None:
      return crrList

    ## now to break the current list into two halfs
    [left, right] = self.breakHalf(crrList)

    ## recurse them and do merge
    return self.merge(self.sortList(left), self.sortList(right))


  #### a helper function to break current list into left and right half
  def breakHalf(self, crrList):
    # find the length of current list
    crr = crrList
    length = 0
    while crr:
      length += 1
      crr = crr.next
    # then find the mid point to break
    mid = crrList
    for i in range(length // 2 - 1):
      mid = mid.next
    # now break list by the mid point
    right = mid.next
    mid.next = None
    return [crrList, right]


  #### this is the original problem 21: merge two sorted array
  def merge(self, l1, l2):
    head = ListNode()
    crr = head
    while l1 and l2:
      if l1.val < l2.val:
        crr.next = ListNode(l1.val)
        crr = crr.next
        l1 = l1.next
      else:
        crr.next = ListNode(l2.val)
        crr = crr.next
        l2 = l2.next
    if l1: crr.next = l1
    if l2: crr.next = l2
    return head.next


## Run code after defining input and solver
input = ListNode().create([-4,9,5,7,2,0,1])
solver = Solution().sortList
print(solver(input).show())