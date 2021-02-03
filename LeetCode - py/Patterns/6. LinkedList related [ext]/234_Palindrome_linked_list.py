'''
Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
'''

# Import helper class ListNode in this folder
# It is the same as LeetCode one with additional methods show() and create()
from ListNode import ListNode

class Solution:
  '''
  MY CODE VERSION
  Thought:
    The first idea came up was using stack for the most palindrome questions
      - First pass through list to push the value to a stack
      - Second pass through list to pop stack from top 
    Finally the stack should be empty
  Iteration:
    This method requires a stack in O(n). If follow up, we cannot use stack to store information
    One possible way is to reverse the second half of list
    And use two pointers to check. I won't present this method here since 实际应用这样之太无聊了吧 代码又繁琐
  Complexity:
    Time: O(n)
    Space: O(n)
  '''
  def isPalindrome(self, head: ListNode) -> bool:
    crr = head
    stack = []
    # first pass to record list value in a stack
    while crr:
      stack.append(crr.val)
      crr = crr.next
    # second pass to check list with the top of stack
    crr = head
    while crr:
      if crr.val == stack[-1]:
        stack.pop()
        crr = crr.next
      else:
        return False
    
    return True


## Run code after defining input and solver
input = ListNode().create([1,2,2,3,3,2,2,1])
solver = Solution().isPalindrome
print(solver(input))