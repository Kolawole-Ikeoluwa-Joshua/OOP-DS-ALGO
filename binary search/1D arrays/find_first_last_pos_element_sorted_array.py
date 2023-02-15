'''
Given an array of integers nums sorted in non-decreasing order, 

find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

'''

class Solution:
    def findFirstLast(self, arr, n, x):
        '''
        approach use binary search to find first and last occurance
        Time: O(log n)
        Space: O(1)
        
        '''
        # code
        v = []
    
        res = -1
        l = 0
        r = n - 1
    
        while l<=r:
            m = l+(r-l)//2
        
            if arr[m] == x:
                res = m
                r = m - 1
            
            elif arr[m] > x:
                r = m -1
            
            else:
                l = m+1
            
        v.append(res)
    
        l = 0
        r = n - 1
    
        while l<=r:
            m = l+(r-l) //2
        
            if arr[m] == x:
                res = m
                l = m + 1
            
            elif arr[m] > x:
                r = m - 1
            
            else:
                l = m + 1
            
        v.append(res)
    
        return v    

    
ob = Solution()
ans = ob.findFirstLast(arr=[1, 3, 5, 5, 5, 5, 67, 123, 125], n=9, x=5)
print(ans)