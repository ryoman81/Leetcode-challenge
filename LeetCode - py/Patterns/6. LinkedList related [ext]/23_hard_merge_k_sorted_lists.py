'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
 
Constraints:
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
'''

# Import helper class ListNode in this folder
# It is the same as LeetCode one with additional methods show() and create()
from ListNode import ListNode

class Solution:
  '''
  OPTIMAL CODE VERSION
  Improvement:
    Improved from my code version by merge two lists and replace the result in place
    This reduce the space complexity to 1
  Complexity:
    Time: O(Nlogk) [!! NOTE: I though the overall merge times should be O(k) instead.. cannot figure out]
    Space: O(1)
  '''
  def mergeKListsOpt(self, lists):
    if len(lists) == 0: return None

    n = len(lists)
    while n > 1:
      # define a k as the mid point
      # e.g. [1,4,6,7,8] len=5 i=0 k=3
      # e.g. [2,4,5,8] len=4 i=0 k=2
      k = (n + 1) // 2
      for i in range(0, n//2): 
        lists[i] = self.merge2Lists(lists[i], lists[i+k])
      # before entering the next loop, we should update n, the total lists we need to merge
      n = k
    # after the while-loop there should be only one list in the array
    return lists[0]

  '''
  MY CODE VERSION
  Thought:
    As the title, the key of merge k lists is how to devide the problem into sub-problem of merge 2 list
    The optimal solution is like Merge Sort, that recursively merge two pair of lists until there is only one
    Here I did not use recursion but
      - a while-loop to iterate pairs
      - an additional array newLists to record the current group of lists to be merged 
      - update length n and lists array at each iteration
  Complexity:
    Time: O(Nlogk)  for each merge2lists it costs O(N) and O(logk) for the times of merge [!! NOTE: I though it should be O(k) instead.. cannot figure out]
    Space: O(k)     could be reduced to O(1) if updating lists array directly
  '''
  def mergeKLists(self, lists):
    if len(lists) == 0: return None
    if len(lists) == 1: return lists[0]
    
    left = lists[0]
    right = lists[1]

    n = len(lists)
    while n > 1:
      newLists = []
      for i in range(0, n, 2):    
        left = lists[i]
        if i+1 < n:
          right = lists[i+1]
          newLists.append(self.merge2Lists(left, right))
        else:
          newLists.append(left)

      n = len(newLists)
      lists = newLists

    return lists[0]

  ## This is original code from problem 21 that merge two sorted lists
  def merge2Lists(self, l1, l2):
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
    if l1:
      crr.next = l1
    if l2:
      crr.next = l2
    return head.next
    

## Run code after defining input and solver
list1 = ListNode().create([1,4,5])
list2 = ListNode().create([1,3,4])
list3 = ListNode().create([2,6])
solver = Solution().mergeKListsOpt
print(solver([list1, list2, list3]).show())