'''
Given a sorted array arr[] of size N without duplicates, and given a value x. 
Floor of x is defined as the largest element K in arr[] 
such that K is smaller than or equal to x. Find the index of K(0-based indexing).

'''

class Solution:
    def findFloor(self, arr, n, x):

        lo = 0
        hi = n-1

        while lo <= hi:

            mid = lo + (hi - lo) // 2

            if arr[mid] > x:
                hi = mid - 1
            else:
                lo = mid + 1

        return lo - 1



ob = Solution()
ans = ob.findFloor(arr=[1,2,8,10,11,12,19], n=7, x=5)
print(ans)