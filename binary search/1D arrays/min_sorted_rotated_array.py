'''
A sorted(in ascending order) array A[ ] with distinct elements is rotated at some unknown point, the task is to find the minimum element in it.

'''

class Solution:
    def minSearch(self, nums):
        # code here

        '''
        note:
        find the index value, then always use while (left < right)
        need to return the index during the search, use while (left <= right)

        Time: O(log n)
        Space: O(1)
        
        '''
        l = 0
        r = len(nums)-1

        while l < r:
            m = l + (r-l) // 2
            # the pivot must be to the right of the middl
            if nums[m] > nums[r]:
                l = m + 1

            # the pivot must be to the left of the middl
            else:
                r = m


        # so we shrink the left/right bounds to one value,
        # without ever disqualifying a possible minimum   
        return nums[l]




ob = Solution()
ans = ob.minSearch(nums=[10, 20, 30, 40, 50, 5, 7])
print(ans)