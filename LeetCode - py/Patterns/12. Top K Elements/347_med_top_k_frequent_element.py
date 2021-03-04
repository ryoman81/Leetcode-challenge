'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.
'''


# Import helper class maxHeap in this folder
import heapq

class Solution:
  '''
  OPTIMAL CODE VERSION
  Thought:
    The improvement of this solution is the sorting step, where we maintain a k size minHeap
      - Once we created a hash table and its representative [ [key1, val1], [key2, val2], ... ]
      - We heapify a k size heap from the first k items's value of hashTable
      - then we compare the remaining (N-k) elements with the top of the minheap
        - if item.val <= top, leave it alone 
        - if item.key > top, we extract (pop) the top of heap (O(logk)) and insert this item (O(logk))
  
    PLEASE NOTE: Our own minHeap class cannot achieve this since it doesn't accept hashtable or tuple as input...
                 We have to use a library heapq to achieve this... 
                 我收回introduction里头那个话,, 这题真没法纯手工再写一个heap的insert和extract方法, 要不然代码量太大了
                 我自己写的heap类只支持数组元素为单个值得操作, 不支持iterate一个键值对数组[key, val]
  Complexity:
    Time: O(nlogk)
    Space: O(n)
  '''
  def topKFrequentOpt(self, nums, k):
    # first create a hash table to record to the frequency of each unique number  // O(n)
    hashTable = {}
    for item in nums:
      if item in hashTable:
        hashTable[item] += 1
      else:
        hashTable[item] = 1

    # we convert hashTable to an array of tuple such like [[key1, val2], [[key2,val2]]  // O(n)
    freqList = []
    for key in hashTable:
      freqList.append([key, hashTable[key]])

    # now the magic is using heapq library............
    # it provides a method based on heap that returns the largest k element in an iterable object
    # this step takes O(nlogk)
    topK = heapq.nlargest(k, freqList, key=lambda item: item[1])

    # return the result
    res = []
    for item in topK:
      res.append(item[0])
    return res

  '''
  MY CODE VERSION
  Thought:
    Without using a heap (as this topic says), the whole workflow is traightforward
      - create a hash map to store the frequencies of each unique number
      - create a list to represent the [ [key1, val1], [key2, val2], ... ]
      - sort this list reversely by the values (frequencies)
      - return the top k items[0] (because we only want key, not the frequency)
    The pain point of this solution is the sorting step which costs nlogn
  Complexity:
    Time: O(2n+nlogn) = O(nlogn)
    Space: O(n)
  '''
  def topKFrequent(self, nums, k):
    # first create a hash table to record to the frequency of each unique number  // O(n)
    hashTable = {}
    for item in nums:
      if item in hashTable:
        hashTable[item] += 1
      else:
        hashTable[item] = 1

    # we convert hashTable to an array of tuple such like [[key1, val2], [[key2,val2]]  // O(n)
    freqList = []
    for key in hashTable:
      freqList.append([key, hashTable[key]])

    # then we sort this list by the frequency  // O(nlogn)
    freqList.sort(key=lambda item: item[1], reverse=True)

    # return the first k of freqList
    result = []
    for i in range(k):
      result.append(freqList[i][0])
    
    return result
      

## Run code after defining input and solver
input1 = [1,1,1,1,1,2,5,5,5,5]
input2 = 2
solver = Solution().topKFrequentOpt
print(solver(input1, input2))