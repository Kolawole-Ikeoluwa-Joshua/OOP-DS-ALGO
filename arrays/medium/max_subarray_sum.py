'''
Q1.
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
        # maximum contiguous subarray sum that ends at current index i
        curr_max = 0

        # maximum contiguous subarray sum we have seen so far
        max_so_far = float('-inf')

        # storing the max sum at each iteration
        for element in arr:
            curr_max = max(element, curr_max+element)
            max_so_far = max(max_so_far, curr_max)

        return max_so_far

        # solution 3 divide and conquer??


    '''
    Q2.
    Print the Largest Sum Contiguous Subarray 
    '''

    def printMaxSubArraySum(self, arr, n):

        start = 0 # start index of maximum contiguous subarray sum that ends at a current index i
        end = 0 # end index of maximum contiguous subarray sum that ends at a current index i

        maxi = 0

        s = 0
        sum = 0

        for i in range(n):
            # get maximum contiguous subarray sum that ends at a current index i
            sum += arr[i]


            # update start and end of the contiguous subarray
            if maxi < sum:
                
                maxi = sum
                start = s
                end = i


            if sum < 0:
                sum = 0
                s = i + 1

        return arr[start:end+1]





# Q1.
ob = Solution()
ans = ob.maxSubArraySum(arr=[1,2,3,-2,5], n=5)
print(ans)

#Q2.

ob = Solution()
ans = ob.printMaxSubArraySum(arr=[1,2,3,-2,5], n=5)
print(ans) 