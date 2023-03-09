'''
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.
'''


class Solution:
    def findKthPositive(self, arr, k):

        '''
        Time: O(logn)
        Space: O (1)
        '''
        # code here

        l = 0
        r = len(arr)

        while l < r:

            m = l + (r-l)//2

            '''
            check if there are k missing integers between A[0] and A[m]

            To check this, subtract the value of A[m] from its index m and subtracting the value of A[0] from its index 0. 
            
            The difference between these two values will give us the number of missing integers up to A[m].
            '''

            if arr[m] - 1 - m < k:
                #  the kth missing integer is not in the range [A[0], A[m]].
                l = m + 1
            else:
                r = m
        # if no missing integer in between search range, return l + k
        return l + k



ob = Solution()
ans = ob.findKthPositive(arr=[2,3,4,7,11], k=5)
print(ans) 