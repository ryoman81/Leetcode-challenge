'''
Write a program to find the node at which the intersection of two singly linked lists begins.

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
 
Example 2:
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
 
Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.

Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Each value on each linked list is in the range [1, 10^9].
Your code should preferably run in O(n) time and use only O(1) memory.
'''

class Solution:
  '''
  MY CODE VERSION
  Thought:
    Due to specific problem setting, we are not going to create such a run case. Please run it in LeetCode environment
    To find the intersection, we need to find a time that pointerA == pointerB
    Since two lists may not be the same length, what we will do are:
      1. find the length of both lists
      2. advance the pointer in the longer list until two pointers will go through the same length to the end
      3. start looping through two lists using two pointers
      4. return when two pointers pointing to the same node
      5. otherwise return null
  Complexity:
    Time: O(n)
    Space: O(1)
  '''
  def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    # STEP1: first pass to find the length of both list
    lenA = 0
    crrA = headA
    while crrA:
      lenA += 1
      crrA = crrA.next
    lenB = 0
    crrB = headB
    while crrB:
      lenB += 1
      crrB = crrB.next
    
    # reset the pointers of A and B
    crrA = headA
    crrB = headB
    
    # STEP2: advance the point of longer list by abs(lenA-lenB) steps
    if lenA > lenB:
      for i in range(lenA-lenB):
        crrA = crrA.next
    else:
      for i in range(lenB-lenA):
        crrB = crrB.next
    
    # STEP3: march both pointers together until they meet or to the end
    while crrA:
      if crrA == crrB:
        return crrA
      else:
        crrA = crrA.next
        crrB = crrB.next
            
    return None


## Run code after defining input and solver
## In this example I am not going to create such a list with intersection...