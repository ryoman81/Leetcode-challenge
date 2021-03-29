'''
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, 
all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1
 
Constraints:
1 <= bad <= n <= 231 - 1
'''

def isBadVersion (n):
  if n >= 33754:
    return True
  else:
    return False

class Solution:
  '''
  MY CODE VERSION
  Thought:
    - Same as the 34 the part that search for the left boundary
    - Hence the point is to exhaust the while loop and return the meeting point (left and right hit together, usually use left)
    - special point is: the indexing started from 1 but we still follow left and right close rule [left, right] not [left, right)
  Complexity:
    Time: O(logn)
    Space: O(1)
  '''
  def firstBadVersion(self, n):
    left = 1
    right = n
    
    while left <= right:
      mid = left + (right-left)//2
      
      # this is the same expression of: if(nums[mid] < target)
      if not isBadVersion(mid):
        left = mid + 1
      else:
        right = mid - 1

    return left

## Run code after defining input and solver
input = 100000
solver = Solution().firstBadVersion
print(solver(input))