'''
Given an unsorted array Arr[] of N integers and an integer X, find floor and ceiling of X

Floor of X is the largest element which is smaller than or equal to X. 
Floor of X doesnt exist if X is smaller than smallest element of Arr

Ceil of X is the smallest element which is greater than or equal to X. 
Ceil of X doesnt exist if X is greater than greatest element of Arr

'''
class Solution:
    def getFloorAndCeil(self, arr, n, x):
        # code here

        '''
        two pointer approach
        Time: O(n)
        Space: O(1)
        '''
        f = -1
        c = float('inf')

        for i in range(n):
            if arr[i] <= x:
                f = max(arr[i], f)

            if arr[i] >= x:
                c = min(arr[i], c)

        if c == float('inf'):
            c = -1

        return [f,c]



ob = Solution()
ans = ob.getFloorAndCeil(arr=[5,6,8,9,6,5,5,6], n=8, x=7)
print(ans)