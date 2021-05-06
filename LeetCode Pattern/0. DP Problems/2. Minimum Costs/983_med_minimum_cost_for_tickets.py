'''
In a country popular for train travel, you have planned some train travelling one year in advance.  
The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.
Train tickets are sold in 3 different ways:
a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.
For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.

Example 1:
Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.

Example 2:
Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total you spent $17 and covered all the days of your travel.
 
Note:
1 <= days.length <= 365
1 <= days[i] <= 365
days is in strictly increasing order.
costs.length == 3
1 <= costs[i] <= 1000
'''


class Solution:
  '''
  MY CODE VERSION
  Thought:
    Dynamic Programming template:
      State: DP[n] - the minimum cost to travel and the previous ticket covers nth day
      Transition: DP[n] = min(DP[n-1]+cost[0], DP[n-7]+cost[1], DP[n-30]+cost[2])
                  if the nth day has no travel, DP[n] = DP[n-1] (this is the hard point to think about)
      Initial states: DP[0]=0
  Complexity:
    Time: O(366)
    Space: O(366)
  '''
  def mincostTickets(self, days, costs):
    lastDay = days[-1]
    # Create DP from day 0 to the last day
    DP = [float('inf')] * (lastDay+1)
    # Initialize DP at day 0
    DP[0] = 0

    # Construct DP by looping over days
    for i in range(1, lastDay+1):
      if i not in days:
        DP[i] = DP[i-1]
        continue
    
      DP[i] = min(DP[i-1]+costs[0], DP[max(0, i-7)]+costs[1], DP[max(0, i-30)]+costs[2])

    # finally find the minimum cost covering until the last day
    return DP[-1]


## Run code after defining input and solver
input1 = [1,4,6,7,8,20]
input2 = [7,2,15]
solver = Solution().mincostTickets
print(solver(input1, input2))