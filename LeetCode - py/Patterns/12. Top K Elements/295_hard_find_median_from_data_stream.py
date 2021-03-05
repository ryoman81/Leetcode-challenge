'''
Median is the middle value in an ordered integer list. If the size of the list is even, 
there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3
[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:
void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 
Example:
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 
Follow up:
If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
'''


# Import helper class maxHeap in this folder
from Heap import minHeap
from Heap import maxHeap

class MedianFinder:
  def __init__(self):
    self.size = 0
    # data structure 1: a sorted array
    self.sortedArr = []
    # data stureture 2: two heaps
    self.minHeap = minHeap()
    self.maxHeap = maxHeap()

  '''
  Solution 1
  Thought:
    This is a very straightforward solution that we maintain a sorted list.
    This solution is very slow (submission 8456ms) due to add method
      Data structure: 
        + sorted list
      Add method: O(n)
        + add to the position where maintain the sorted property 
        + we can either use brute force or binary search to locate the position to insert
        + however, either method may occur O(n) due to .insert method that changed the array
      Find median method: O(1)
        + lookup for the middle element 
      Space complexity: O(n)
  '''
  def addNum1(self, num):
    # check if append to the last position
    if not self.sortedArr or num >= self.sortedArr[-1]:
      self.sortedArr.append(num)
    # else then find the first item that larger than the input number
    # NOTE:: An improvement can be done by using binary search to locate the postion to insert O(logn)
    #        However, to the inserting step using built-in method may still have O(n) complexity to change the size of array
    else:
      for i in range(self.size):
        if self.sortedArr[i] > num:
          self.sortedArr.insert(i, num)
          break
    # increment size and return
    self.size += 1
    return

  def findMedian1(self):
    # if odd, find the middle index
    if self.size % 2:
      return self.sortedArr[self.size//2]
    # if even, find the middle two elements
    else:
      first = self.sortedArr[int(self.size/2 - 1)]
      second = self.sortedArr[int(self.size/2)]
      return (first+second) / 2


  '''
  Solution 2
  Thought:
    This is the topic method that very suitable for this problem
      - We maintain one max heap to store all smaller half of numbers
      - We maintain one min heap to store all larger half of numbers
      - The top of both max heap and min heap will be the median value of entire numbers
      Data structure:
        + min heap
        + max heap 
      Add method: O(logn * 5)
        + please see the comments below
      Find median method: O(1)
        Finding median has constant complexity since we only care the top of max and min heaps
      Space compexity: O(n) 
  '''
  def addNum(self, num):
    # everytime when an incoming we insert it to the maxHeap, which is the smaller half of all numbers
    self.maxHeap.insert(num)
    # and we will extract the top and put it into the minHeap, which is the larger half
    val = self.maxHeap.extract()
    self.minHeap.insert(val)

    # the two steps above gaurantee that the maxheap maintain all smaller numbers and minheap maintain all larger numbers
    # but we want to keep both heaps have the same size (or maxheap is one number more than minheap)
    # sometimes, the minheap will be one number more than than maxheap after above steps (odd total numbers)
    if self.minHeap.size > self.maxHeap.size:
      # in this case we extract top from min heap and insert it to the max heap
      val = self.minHeap.extract()
      self.maxHeap.insert(val)
    
    # after all the steps, we are successfully maintaining the states that:
    #   1. max heap has all smaller numbers
    #   2. min heap has all larger numbers
    #   3. max heap size equals (or has one more number) compared to min heap
    #   4. the top of heaps is/are median!!
    return

  def findMedian(self):
    size = self.minHeap.size + self.maxHeap.size
    if size % 2:
      return self.maxHeap.getMax()
    else:
      return (self.maxHeap.getMax() + self.minHeap.getMin()) / 2


## Run code after defining input and solver
# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(2)
obj.addNum(3)
print(obj.findMedian())
obj.addNum(4)
print(obj.findMedian())