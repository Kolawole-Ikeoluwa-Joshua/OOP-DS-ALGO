'''
Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, 
divide all the array by it, and sum the division's result. 
Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of the division is rounded to the nearest integer greater than or equal to that element. 
(For example: 7/3 = 3 and 10/2 = 5).

'''

class Solution:
    def smallestDivisor(self, nums, threshold):

        '''
        Time: O(nlog(max(nums)))
        Space: O(1)
        '''

        # code here

        def condition(divisor):

            # find ceil division of num in nums & divisor then, get total sum
            # return true or false if sum <= threshold

            return sum((num - 1) // divisor + 1 for num in nums) <= threshold




        left, right = 1, max(nums)
        while left < right:

            mid = left + (right - left)//2

            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left


ob = Solution()
ans = ob.smallestDivisor(nums=[44,22,33,11,1], threshold=5)
print(ans)



