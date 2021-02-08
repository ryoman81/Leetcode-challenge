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
      - Also initiate two variable that store the current highest bar at leftside and right side
      - Move starts from a shorter one and moving centerwards, now we have some actions
        - if meet a shorter bar, count on the 洼地
        - if meet a higher bar, update higher bar instead
      - 
  Complexity:
    Time: O(n)
    Space: O(1)
  '''
  def maxArea(self, height):
    left = 0
    right = len(height) - 1

    area = 0

    while left < right:
      crrArea = (right - left) * min([height[left], height[right]])
      if crrArea > area:
        area = crrArea
      
      if height[left] < height[right]:
        left += 1
      else:
        right -= 1

    return area
    

## Run code after defining input and solver
input1 = [4,3,2,1,4]
solver = Solution().maxArea
print(solver(input1))