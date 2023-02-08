'''
Implement the next permutation, which rearranges the list of numbers into Lexicographically next greater permutation of list of numbers. 
If such arrangement is not possible, it must be rearranged to the lowest possible order i.e. sorted in an ascending order. 
You are given an list of numbers arr[ ] of size N.

'''

class Solution:
    def nextPermutation(self, nums):

        '''
        using swap and reverse approach

        time: O(n)
        Space: O(1)
        '''


        n = len(nums) - 1
        # pivot index
        p = -1
        # pivot value
        pv = 0

        # first find decreasing element from the end of the list
        for i in range(n-1, -1, -1):
            if nums[i] < nums[i+1]:
                # if found set pivot index and value
                p = i
                pv = nums[i]
                break

        # if no decreasing element is found, return reversed list as next permutation         
        if p == -1:
            nums.reverse()
            return

        # if pivot has been found
        # find first element greater than pivot from end of list
        for i in range(n, -1, -1):
            # if found, swap element and pivot value
            if nums[i] > pv:
                nums[i], nums[p] = nums[p], nums[i]
                break

        # reverse elements after the pivot index
        nums[p+1:] = nums[p+1:][::-1]

        return nums



ob = Solution()
ans = ob.nextPermutation(nums=[1, 2, 3, 6, 5, 4])
print(ans)