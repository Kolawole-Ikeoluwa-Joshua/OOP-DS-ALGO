'''
Given an array A of positive integers. Your task is to find the leaders in the array. 
An element of array is leader if it is greater than or equal to all the elements to its right side. 
The rightmost element is always a leader. 
'''

class Solution:
    def leaders(self, A, N):

        '''
        approach: find leaders from right side
        Time: O(n)
        Space: O(n)
        
        '''
        ans = []
        max = A[N-1]

        for i in range(N-1, -1,-1):
            if A[i] >= max:
                max = A[i]
                ans.append(A[i])

        # reverse array ans
        ans[0:] = ans[0:][::-1]
        return ans


ob = Solution()
ans = ob.leaders(A=[16,17,4,3,5,2], N=6)
print(ans)