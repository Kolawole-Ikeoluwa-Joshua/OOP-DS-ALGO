'''
Given two unsorted arrays A of size N and B of size M of distinct elements, 
the task is to find all pairs from both arrays whose sum is equal to X.

Note: All pairs should be printed in increasing order 

'''

class Solution:
        
    def allPairs(self, A, B, N, M, X):
        # Your code goes here 
        res = []
        A.sort()
        
        for i in range(len(A)):
            # check if pair of element in array A is in array B
            if X - A[i] in B:
                res.append([A[i], X - A[i]])
        return res

ob = Solution()
ans = ob.allPairs(A=[1, 2, 4, 5, 7], B=[5, 6, 3, 4, 8], N=5, M=5, X=9)
print(ans)
