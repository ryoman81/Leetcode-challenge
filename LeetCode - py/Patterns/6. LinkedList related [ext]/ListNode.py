### Data structure of Linked list node
### Created for minicing LeetCode internal list structure

class ListNode:
  # define constructor function as defined in LeetCode
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

  # a helping method to show the linked list as an array
  def show (self):
    crr = self
    # if empty list then return an empty array
    if crr == None:
      return []
    # otherwise create an array with list value
    arr = [crr.val]
    while crr.next != None:
      crr = crr.next
      arr.append(crr.val)
    return arr

  # a helping method to create a linked list given an array
  def create (self, arr):
    # if array is empty, return None
    if len(arr) == 0:
      return None
    # otherwise create such a list
    head = ListNode(arr[0])
    crr = head
    for i in range(1,len(arr)):
      crr.next = ListNode(arr[i])
      crr = crr.next
    return head