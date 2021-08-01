class MyStack:

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.main = []      # main stack simulated by queue
    self.help = []      # helping queue structure
    self.topE = None
      

  def push(self, x: int) -> None:
    """
    Push element x onto stack.
    """
    self.main.append(x)
    self.topE = x
      

  def pop(self) -> int:
    """
    Removes the element on top of the stack and returns that element.
    """
    if len(self.main) == 0:
      return None
    elif len(self.main) == 1:
      self.topE = None
      return self.main.pop(0)
    else:
      while len(self.main) > 1:
        self.topE = self.main.pop(0)
        self.help.append(self.topE)
    
      out = self.main.pop(0)
      self.main = self.help[:]
      self.help = []
      return out
      

  def top(self) -> int:
    """
    Get the top element.
    """
    return self.topE
      

  def empty(self) -> bool:
    """
    Returns whether the stack is empty.
    """
    if self.topE:
        return False
    else:
        return True
        


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(5)
obj.push(2)
obj.push(4)
obj.push(8)

val = obj.top()
val = obj.pop()
val = obj.top()
val = obj.pop()
val = obj.top()
val = obj.pop()
val = obj.top()
val = obj.pop()
val = obj.top()
val = obj.pop()