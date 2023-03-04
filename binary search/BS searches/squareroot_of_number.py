'''
Given an integer x, find the square root of x. If x is not a perfect square, then return floor(√x).
'''

class Solution:
    def squareRoot(self, x):

        '''
        Time: O(log n)
        Space: O(1)
        
        '''
        l  = 0
        r = x

        while l <= r:
            mid = (r+l)//2

            if mid * mid == x:
                return mid
            elif mid * mid > x:
                r = mid - 1
            else:
                l = mid + 1
                ans = mid
        return ans


ob = Solution()
ans = ob.squareRoot(x=5)
print(ans)








