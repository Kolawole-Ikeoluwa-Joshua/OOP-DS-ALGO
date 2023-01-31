'''
Given a binary array arr of size N and an integer M. 
Find the maximum number of consecutive 1's produced by flipping at most M 0's.
'''

class Solution:
    def findZeroes(self, arr, n, m):

        # code here
        # sliding window method
        maxConsecOne = 0
        start = 0
        zeroCount = 0

        for i in range(0, n):
            if arr[i] == 0:
                zeroCount += 1

            while zeroCount > m:
                if arr[start] == 0:
                    zeroCount -= 1
                
                start += 1

            maxConsecOne = max(maxConsecOne, i-start+1)

        return maxConsecOne


ob = Solution()
ans = ob.findZeroes(arr=[1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1], n=11, m=2)
print(ans)