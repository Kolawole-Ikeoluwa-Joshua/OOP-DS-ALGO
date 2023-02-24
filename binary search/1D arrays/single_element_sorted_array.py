'''
Given a sorted array arr[] of size N. Find the element that appears only once in the array. All other elements appear exactly twice. 
'''


'''

approach:


Time: O(log n)
Space: O(1)
'''

class Solution:
    def findSingle(self, arr, n):
        l = 0
        r = n -1

        while l < r:
            m = l + (r-l)//2


            # if mid is even, then it's duplicate should be in next index.
	        # if mid is odd, then it's duplicate  should be in previous index.
            # if any of these conditions are satisified then duplicates exist, need to check in next half of array i.e left = mid + 1
            if m % 2 == 0 and arr[m] == arr[m+1] or m % 2 == 1 and arr[m-1] == arr[m]:
                l = m + 1

            else:
                r = m

        return arr[l]


ob = Solution()
ans = ob.findSingle(arr=[1, 1, 2, 2, 3, 3, 4, 50, 50, 65, 65], n=11)
print(ans)