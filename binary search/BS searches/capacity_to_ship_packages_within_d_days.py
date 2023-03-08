'''
A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. 

Each day, we load the ship with packages on the conveyor belt (in the order given by weights). 

We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.
'''


class Solution:
    def function(self, weights, days):

        '''
        Time: O(N*log(sum(weights)))
        Space: O(1)
        '''
        # code here

        # feasible function
        def feasible(capacity):
            day = 1
            total = 0

            for weight in weights:
                total += weight
                if total > capacity:
                    total = weight
                    day += 1
                    if day > days:
                        return False
            return True

        # search for minimum capacity between max weight and total weights
        left = max(weights)
        right = sum(weights)

        while left < right:

            mid = left + (right - left)//2
            # verify if selected minimum capacity can ship all packages
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left



ob = Solution()
ans = ob.function(weights=[1,2,3,4,5,6,7,8,9,10], days=5)
print(ans) 