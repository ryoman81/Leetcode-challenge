'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by input 
In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    记得是当时挺难的一道题, 回头看了下js的代码也不知所云. 现在确定好是two pointers两边相向的方案就来研究实现的过程
      - Initiate two pointers left and right
      - Also initiate two variable that store the current highest bar at left side and right side
      - Move starts from a shorter one and moving centerwards, now we have some actions
        - if meet a shorter bar, count on the 洼地 that is the difference between max and this value
        - if meet a higher bar, update pointer and higher bar instead, and stop moving
      - For each iteration we should campare left and right and to work on the shorter bar
        (at each iteration, this is a VERY important step. We should always work on a shorter side
         to gaurantee there is a 洼地 between left and right. e.g. [4,1,1,1] if we not start and 
         iterate from 1 (the right side), then the left pointer will never no if there is any boundary
         on its right. 水都从右边流掉了...)
  Complexity:
    Time: O(n)
    Space: O(1)
  '''
  def trap(self, height):
    # error check if input array is empty
    if len(height) == 0:
      return 0

    left = 0
    right = len(height) - 1
    leftMax = height[left]
    rightMax = height[right]

    result = 0

    while left < right:
      # check which side to work on. we always work on the shorter side
      if height[left] <= height[right]:
        cnt = 1
        while left + cnt < right and height[left+cnt] < leftMax:
          result += leftMax - height[left+cnt]
          # advance counting pointer
          cnt += 1
        # advance left pointer by cnt
        left += cnt
        # if while-loop break, check if not meet right 
        if left < right:
          # if not meet right then it must meet a higher or equal bar
          leftMax = height[left]
        
      else:
        cnt = 1
        while right - cnt > left and height[right-cnt] < rightMax:
          result += rightMax - height[right-cnt]
          # advance counting pointer
          cnt += 1
        # advance right pointer
        right -= cnt
        # if while-loop break, check if not meet left 
        if right > left:
          # if not meet left then it must meet a higher or equal bar
          rightMax = height[right]
        
    return result
    

## Run code after defining input and solver
input1 = [4,1,1,1,1]
solver = Solution().trap
print(solver(input1))