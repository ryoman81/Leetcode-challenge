class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

  def show (self):
    crr = self
    arr = [crr.val]
    while crr.next != None:
      crr = crr.next
      arr.append(crr.val)
      
    return arr