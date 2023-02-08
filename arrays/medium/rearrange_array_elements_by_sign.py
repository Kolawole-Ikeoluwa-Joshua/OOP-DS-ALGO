'''
Given an unsorted array Arr of N positive and negative numbers. 
Your task is to create an array of alternate positive and negative numbers 
without changing the relative order of positive and negative numbers.
Note: Array should start with a positive number.

'''

class Solution:
    def rearrangeArray(self,arr):

        '''
        approach: we know that in the rearranged array, positive numbers will have indices that are mmultiples of 2 i.e (0,2,4...),
        and negative numbers will have odd indices i.e (1,3,...)

        using two pointers

        Time: O(n)
        Space: O(n)
        
        '''
        # code here

        a = [0] * len(arr)

        p = 0
        n = 1

        for i in range(len(arr)):
            if arr[i] >= 0:
                a[p] = arr[i]
                p += 2

            else:
                a[n] = arr[i]
                n += 2

        return a


ob = Solution()
ans = ob.rearrangeArray(arr=[9, 4, -2, -1, 5, 0, -5, -3, 2])
print(ans)