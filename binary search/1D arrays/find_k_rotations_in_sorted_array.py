'''
Given an ascending sorted rotated array Arr of distinct integers of size N. 

The array is right rotated K times. Find the value of K.

Time: O(log n)
Space: O(1)

'''

class Solution:
    def findKRotation(self, arr, n):
        start = 0
        end = n-1

        # using binary search
        while start <= end:
            # when array is already sorted
            if arr[start] <= arr[end]:
                return start
            
            mid = start + (end - start) // 2

            # calculate next and previous
            next = (mid + 1) % n
            prev = (mid + n - 1) % n

            if arr[mid] <= arr[next] and arr[mid] <= arr[prev]:
                return mid
            
            elif arr[start] <= arr[mid]:
                start = mid + 1 # search right

            else:
                end = mid - 1 # search left

        return 0



ob = Solution()
ans = ob.findKRotation(arr=[5, 1, 2, 3, 4], n=5)
print(ans)