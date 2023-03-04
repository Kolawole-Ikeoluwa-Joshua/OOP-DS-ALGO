'''
You are given 2 numbers (n , m); the task is to find n√m (nth root of m).
'''

class Solution:
    def nthRoot(self, n, m):

        '''
        Time: O(n * log m)
        Space: O(1)
        '''
        
        # code here

        l = 0
        r = m

        while l <= r:
            mid = (r+l)//2

            if mid ** n == m:
                return mid
            elif mid ** n > m:
                r = mid - 1
            else:
                l = mid + 1
        return -1
    

ob = Solution()
ans = ob.nthRoot(n=3, m=9)
print(ans)