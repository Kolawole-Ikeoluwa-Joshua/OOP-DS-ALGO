'''
You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

'''

class Soluton:
    def minDays(self, bloomDay, m, k):

        '''
        approach: # check min days possible to make m bouquets of k flowers using the given list of bloomDay
        Time: O(N * Log(max(bloomDay)))
        Space: O(1)
        
        '''

        #code here


        # create a function to check if m bouquets of k flowers can be made in mid days
        def feasible(days):
            bouquets, flowers = 0, 0

            for bloom in bloomDay:
                # If the bloom occurs after the given number of days
                if bloom > days:
                    flowers = 0
                
                # compute the number of bouquets that can be made with the current count of flowers
                else:
                    bouquets += (flowers + 1)//k 
                    flowers = (flowers + 1) % k     # number of flowers remaining after making a complete bouquet
            
            return bouquets >= m
                


        # check if it is possible to make m bouquets of k flowers using the given list of bloomDay
        # if not possible
        if len(bloomDay) < m * k:
            return -1
        
        # if possible:
        # use binary search to find min no of days required to make m bouquets of k flowers

        left, right = 1, max(bloomDay)

        while left < right:
            mid = left + (right - left)//2

            if feasible(mid):
                # the minimum number of days required must be less than or equal to the mid
                right = mid
            else:
                #  the minimum number of days required must be greater than the mid
                left = mid + 1


        # when left & right are equal terminates search and return
        return left



ob = Soluton()
ans = ob.minDays(bloomDay=[7,7,7,7,12,7,7], m=2, k=3)
print(ans)