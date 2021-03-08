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
# also import the offcial heap module
import heapq

class Solution:
  '''
  OPTIMAL CODE VERSION
  Thought:
    
  Complexity:
    Time: O(Nlogk) [!! NOTE: I though the overall merge times should be O(k) instead.. cannot figure out]
    Space: O(1)
  '''
  def mergeKLists(self, lists):
    heap = []
    for l in lists:
      if l: heap.append(l.val)
    heapq.heapify(heap)

    result_arr = []
    while heap:   # O(n)
      val = heapq.heappop(heap)   # O(1)
      result_arr.append(val)
      # find which node has this value. This for-loop is not necessary but our heap object can only accept num
      for i in range(len(lists)):
        if lists[i] and lists[i].val == val:
          lists[i] = lists[i].next
          if lists[i]: heapq.heappush(heap, lists[i].val)   # O(logk)
      
    # convert array to list
    head = ListNode(0)
    crr = head
    for item in result_arr:   # O(n)
      crr.next = ListNode(item)
      crr = crr.next
    
    return head.next   

## Run code after defining input and solver
list1 = ListNode().create([1,4,5])
list2 = ListNode().create([1,3,4])
list3 = ListNode().create([2,6])
solver = Solution().mergeKLists
print(solver([list1, list2, list3]).show())