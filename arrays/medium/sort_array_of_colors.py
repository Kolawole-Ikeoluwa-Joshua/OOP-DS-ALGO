'''
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

You must solve this problem without using the library's sort function.
'''

class Solution:
    def sort012(self, arr, n):
        # code here

        # using three pointer approach

        '''Time: O(n), Space: O(1)'''

        low = 0
        mid = 0
        high = n-1

        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

        return arr



ob = Solution()
ans = ob.sort012(arr=[0,2,1,2,0], n=5)
print(ans)