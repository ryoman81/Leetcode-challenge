'''
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:

Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 2:
Input: n = 2
Output: false
 
Constraints:
1 <= n <= 231 - 1
'''

class Solution:
  '''
  OPTIMAL CODE VERSION
  Thought:
    Since we are in the topic of fast slow pointer, let take a look at of this solution
      - It is very similar to the linked list problem 141
      - If no result of 1 meet, the fast point will meet slow pointer eventually
    For this solver, we should be mindful about that fast and slow met at 1
      - for example in such a loop n -> 1 -> 1 -> 1
  Complexity:
    Time: O()
    Space: O(1)
  '''
  def isHappyOpt(self, n):
    fast = n
    slow = n

    while fast != 1:
      slow = self.findNext(slow)
      fast = self.findNext(fast)
      fast = self.findNext(fast)
      
      if fast == slow:
        break
    
    return fast == 1

  '''
  MY CODE VERSION
  Thought:
    This is not a slow fast pointer answer
    We use a hash table to store the number we met
    if the upcome number exists in the hash table, then there is a loop
  Complexity:
    Time: O()
    Space: O()
  '''
  def isHappy(self, n):
    hashTable = {}
    crrN = n
    while crrN != 1:
      crrN = self.findNext(crrN)
      # check the next number has existed in the hash table
      if crrN not in hashTable:
        hashTable[crrN] = 1
      else:
        return False
    return True

  ## Help function to calculate the next number based on the given one
  def findNext (self, n):
    strN = str(n)   # stringfy the int number n
    result = 0
    for i in range(len(strN)):
      result += int(strN[i]) ** 2
    return result


## Run code after defining input and solver
input = 19
solver = Solution().isHappyOpt
print(solver(input))