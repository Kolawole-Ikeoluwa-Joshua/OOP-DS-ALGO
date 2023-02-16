'''
Given a sorted and rotated array A of N distinct elements which is rotated at some point, and given an element key. 
The task is to find the index of the given element key in the array A.
'''

class Solution:
    def search(self, arr, target):
        '''
        Time: O(log n)
        Space: O(1)
        '''
        
        #code here

        l = 0
        r = len(arr)

        while l <= r:
            m = l + (r-l) // 2

            if arr[m] == target:
                return m
            
            # if left half before mid is sorted

            if arr[l] <= arr[m]:

                # search left
                if target >= arr[l] and target < arr[m]:
                    r = m - 1

                else:
                    l = m + 1

            # if right half after mid is sorted
            else:

                if target > arr[m] and target <= arr[r]:
                    l = m + 1
                else:
                    r = m - 1


        return -1



ob = Solution()
ans = ob.search(arr=[4,5,6,7,0,1,2], target=0)
print(ans)