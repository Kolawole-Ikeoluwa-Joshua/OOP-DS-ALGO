'''
Given a sorted array Arr of size N and a number X, you need to find the number of occurrences of X in Arr.


'''

class Solution:
    def count(self, arr, x):

        left = self.binarySearch(arr, x, True)
        right = self.binarySearch(arr, x, False)

        if left == -1 or right == -1:
            return 0

        return right - left + 1
    

    def binarySearch(self, arr, x, leftBias):

        l = 0
        r = len(arr)-1
        res = -1

        # leftBias = [True/False] if false, means rightBias
        while l <= r:
            m = l + (r-l)//2

            if arr[m]==x:
                res = m
                if leftBias:
                    r = m -1
                else:
                    l = m+1

            elif arr[m] > x:
                r = m -1

            else:
                l = m + 1

        return res







ob = Solution()
ans = ob.count(arr=[1, 1, 2, 2, 2, 2, 3], x=2)
print(ans)