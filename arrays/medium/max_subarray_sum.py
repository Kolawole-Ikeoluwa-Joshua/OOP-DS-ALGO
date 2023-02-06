'''
Given an array Arr[] of N integers. 
Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.

'''

class Solution:
    def maxSubArraySum(self, arr, n):

        # Solution 1
        '''
        use brute-force by trying out every possible sub-array in arr and choosing the one with maximum sum.
        Time: O(n^2), Space: O(1)
        

        ans = float('-inf')
        for i in range(n):

            curr_sum = 0
            for j in range(i, n):
                curr_sum += arr[j]
                ans = max(ans, curr_sum)

        return ans
        '''

        # Solution 2

        '''
        use kadane's algorithm
        Time: O(n), Space: O(1)
        '''

        curr_max = 0
        max_so_far = float('-inf')

        for element in arr:
            curr_max = max(element, curr_max+element)
            max_so_far = max(max_so_far, curr_max)

        return max_so_far

        # solution 3 divide and conquer??


ob = Solution()
ans = ob.maxSubArraySum(arr=[1,2,3,-2,5], n=5)
print(ans)