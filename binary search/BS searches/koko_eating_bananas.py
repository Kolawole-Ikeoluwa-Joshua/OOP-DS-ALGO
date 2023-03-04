'''
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 

The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. 

Each hour, she chooses some pile of bananas and eats k bananas from that pile. 

If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
'''
import math
class Solution:
    def minEatingSpeed(self, piles, h):

        '''
        code uses a binary search algorithm to find the minimum eating speed that can eat 
        all the bananas within h hours

        Time: O(n * log(m))
        SpaceL O(1)
        
        '''
        # code here

        l = 1
        r = max(piles)
        minHours = r


        # check whether the current speed k can eat all the bananas within h hours.
        while l <= r:

            k, hours = (l+r)//2, 0

            '''
            computes the number of hours required to eat all the bananas at speed k
            by dividing the number of bananas in each pile by k and rounding up to the nearest integer
        
            '''
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                # can eat all the bananas within h hours at speed mid
                minHours = min(minHours, k)
                r = k - 1
                
            else:
                l = k + 1
               

        # return minimum eating speed
        return int(minHours)



ob = Solution()
ans = ob.minEatingSpeed(piles=[30,11,23,4,20], h=5)
print(ans)