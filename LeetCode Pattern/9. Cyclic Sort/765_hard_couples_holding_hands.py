'''
N couples sit in 2N seats arranged in a row and want to hold hands. 
We want to know the minimum number of swaps so that every couple is sitting side by side. 
A swap consists of choosing any two people, then they stand up and switch seats.
The people and seats are represented by an integer from 0 to 2N-1, the couples are numbered in order, 
the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).
The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat.

Example 1:
Input: row = [0, 2, 1, 3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.

Example 2:
Input: row = [3, 2, 0, 1]
Output: 0
Explanation: All couples are already seated side by side.

Note:
len(row) is even and in the range of [4, 60].
row is guaranteed to be a permutation of 0...len(row)-1.
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    This is an unconventional cyclic sort. It is with more greedy algorithm inside
      - We cannot do cyclic sort to the entire array since it requires the minimum swap numbers
      - The answer that I saw used the concept of cyclic sort that swap elements in-place
    Steps
      1. Initialize a hash table to record the value and its location
      2. Loop over each ODD position and check its corresponding even postion
      3. If not the couple, then find the real husband from hash table and swap them. 
      4. remember to update hash table since the location information has updated.

  Complexity:
    Time: O(n)
    Space: O(n)
  '''
  def minSwapsCouples(self, row):
    # create a hash map for recording the position of each member
    hashTable = {}
    for i in range(len(row)):
      hashTable[row[i]] = i

    result = 0
    # loop over row array at its odd position
    # This is a greedy method where sub-optimal is that a couple are sitting in the current odd-even locations 
    # js: for (let i=0; i<row.length; i+=2) {...}
    for i in range(0, len(row), 2):
      left = row[i]
      # check if left is odd or even. for example if left=3 right=2, if left=2, right=3. This is the way to make couple
      if left % 2 == 0:
        right = left + 1
      else:
        right = left - 1

      # check if need to swap
      if row[i+1] != right:
        # the true location where the husband is
        loc = hashTable[right]
        # update hash table
        hashTable[row[i+1]] = loc
        hashTable[right] = i+1
        # swap i+1 and loc
        row[i+1], row[loc] = row[loc], row[i+1]
        # count up result
        result += 1

    return result


## Run code after defining input and solver
input = [0,2,4,6,7,1,3,5]
solver = Solution().minSwapsCouples
print(solver(input))