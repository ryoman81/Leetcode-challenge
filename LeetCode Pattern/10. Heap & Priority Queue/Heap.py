'''
////////////////////////////////////////////min heap/////////////////////////////////////////////////
'''
class minHeap:
  # Initiate a heap with a list and its size
  def __init__ (self):
    self.heap = []
    self.size = 0


  # Function [private] for sifting up an element when inserting a new element (上浮)
  def _siftUp (self, current):
    # find the index of parent node
    parent = (current - 1) // 2
    
    # loop over until root or meet the requirement (some realization use recursion to sift up)
    while parent >= 0:
      # if this node value is smaller than its parent node value
      if self.heap[current] < self.heap[parent]:
        # swap this node and its parent
        self.heap[current], self.heap[parent] = self.heap[parent], self.heap[current]
      else:
        return
      
      # move up and update index and parent
      current = parent
      parent = (current - 1) // 2


  # Function [private] for sifting down an element when extracting the root node (下沉)
  def _siftDown (self, current):
    # find the index of left child and right child
    leftChild = current * 2 + 1
    rightChild = current * 2 + 2
    
    # loop over until no child or meet the requirement
    while leftChild < self.size:
      # find the minimum child mark it as leftChild index
      minChild = leftChild
      # check if right child exists and right child is smaller than left child
      if rightChild < self.size and self.heap[rightChild] < self.heap[leftChild]:
        minChild = rightChild

      # check if the current node should sift down
      if self.heap[current] > self.heap[minChild]:
        # swap them
        self.heap[current], self.heap[minChild] = self.heap[minChild], self.heap[current]
      else:
        return

      # move down and update indexes
      current = minChild
      leftChild = current * 2 + 1
      rightChild = current * 2 + 2


  # Method to insert an item and sift it up to the correct place // O(logn)
  def insert (self, val):
    self.size += 1            # increase the size property
    self.heap.append(val)     # append val to the tail of heap
    self._siftUp(self.size-1)   # sift up this node if not meet the requirement

  
  # Method to extract (pop) the root value // O(logn)
  def extract (self):
    # if empty then return
    if not self.heap:
      return None
    # extract the first element in the heap (which is the min value)
    root = self.heap[0]
    # move the last element to the top of heap
    self.heap[0] = self.heap[-1]
    # remove the last element
    self.heap.pop()
    # decrement size
    self.size -= 1
    # sift down the top element to the correct place
    self._siftDown(0)
    # return the extracted value
    return root


  # Method of getting the min value of the heap
  def getMin (self):
    if not self.heap:
      return None
    return self.heap[0]


  # Method of creating a heap from a list (array)
  # It is not by inserting array items one by one, but use a linear time to create // O(n)
  def heapify (self, arr):
    if not arr:
      return
    # update self properties
    self.heap = arr
    self.size = len(arr)
    # heapify from the position of N/2 by using siftdown method
    i = self.size // 2
    # O(N/4*1 + N/8*2 + N/16*3 + ... + 1*logN) = O(N)
    while i >= 0:
      self._siftDown(i)
      i -= 1
    # return heapified arr
    return self.heap


'''
////////////////////////////////////////////max heap/////////////////////////////////////////////////
'''
class maxHeap:
  # Initiate a heap with a list and its size
  def __init__ (self):
    self.heap = []
    self.size = 0


  # Function [private] for sifting up an element when inserting a new element (上浮)
  def _siftUp (self, current):
    # find the index of parent node
    parent = (current - 1) // 2
    
    # loop over until root or meet the requirement (some realization use recursion to sift up)
    while parent >= 0:
      # if this node value is larger than its parent node value
      if self.heap[current] > self.heap[parent]:
        # swap this node and its parent
        self.heap[current], self.heap[parent] = self.heap[parent], self.heap[current]
      else:
        return
      
      # move up and update index and parent
      current = parent
      parent = (current - 1) // 2


  # Function [private] for sifting down an element when extracting the root node (下沉)
  def _siftDown (self, current):
    # find the index of left child and right child
    leftChild = current * 2 + 1
    rightChild = current * 2 + 2
    
    # loop over until no child or meet the requirement
    while leftChild < self.size:
      # find the maximum child mark it as leftChild index
      maxChild = leftChild
      # check if right child exists and right child is larger than left child
      if rightChild < self.size and self.heap[rightChild] > self.heap[leftChild]:
        maxChild = rightChild

      # check if the current node should sift down
      if self.heap[current] < self.heap[maxChild]:
        # swap them
        self.heap[current], self.heap[maxChild] = self.heap[maxChild], self.heap[current]
      else:
        return

      # move down and update indexes
      current = maxChild
      leftChild = current * 2 + 1
      rightChild = current * 2 + 2


  # Method to insert an item and sift it up to the correct place // O(logn)
  def insert (self, val):
    self.size += 1            # increase the size property
    self.heap.append(val)     # append val to the tail of heap
    self._siftUp(self.size-1)   # sift up this node if not meet the requirement

  
  # Method to extract (pop) the root value // O(logn)
  def extract (self):
    # if empty then return
    if not self.heap:
      return None
    # extract the first element in the heap (which is the max value)
    root = self.heap[0]
    # move the last element to the top of heap
    self.heap[0] = self.heap[-1]
    # remove the last element
    self.heap.pop()
    # decrement size
    self.size -= 1
    # sift down the top element to the correct place
    self._siftDown(0)
    # return the extracted value
    return root


  # Method of getting the min value of the heap
  def getMax (self):
    if not self.heap:
      return None
    return self.heap[0]


  # Method of creating a heap from a list (array)
  # It is not by inserting array items one by one, but use a linear time to create // O(n)
  def heapify (self, arr):
    if not arr:
      return
    # update self properties
    self.heap = arr
    self.size = len(arr)
    # heapify from the position of N/2 by using siftdown method
    i = self.size // 2
    # O(N/4*1 + N/8*2 + N/16*3 + ... + 1*logN) = O(N)
    while i >= 0:
      self._siftDown(i)
      i -= 1
    # return heapified arr
    return self.heap



'''
heap = maxHeap()
# test of heap inserting
heap.insert(9)
heap.insert(6)
heap.insert(5)
heap.insert(2)
heap.insert(3)
heap.insert(1)
heap.insert(4)
print(heap.heap)
# test of heap extracting  
heap.extract()
print(heap.heap)
# test of heapifing
arr = [1,2,5,8,0]
print(heap.heapify(arr))
'''