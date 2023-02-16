'''
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. 

If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. 

In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.
'''
class Solution:
    def findPeakElement(self, nums):
        # solution 1
        '''
        
        l = 0
        r = n -1
        
        while l < r:
            m = l + (r-l) // 2
            # peak on right side
            if nums[m] < nums[m+1]:
                l = m+1
                    
            else:
                # peak on left side
                r = m
                    
        return l
        '''

        # solution 2 - intuitive approach
        n = len(nums)
        # single element array == peak
        if n == 1:
            return 0
        # last element == peak
        if nums[n-1] > nums[n-2]:
            return n-1

        l = 0
        r = n - 1

        while l<=r:
            m = l + (r-l)//2
            # if mid == peak
            if nums[m-1] < nums[m] and nums[m+1] < nums[m]:
                return m
            # if peak on left side
            elif nums[m-1] > nums[m]:
                r = m -1
            # if peak on right side
            else:
                l = m+1

        return -1  # dummy return statement


ob = Solution()
ans = ob.findPeakElement(nums=[1,2,1,3,5,6,4])
print(ans)