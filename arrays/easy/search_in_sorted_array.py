# Searching an element "k" in a sorted array

class Solution:
    def binarySearch(self, arr, N, K):
        l = 0
        r = N - 1
        
        while l <= r:
            m = (l+r) // 2
            
            if arr[m] == K:
                return 1
                
            elif arr[m] > K:
                r = m - 1
                
            else:
                l = m + 1
                
        return -1        



ob = Solution()
ans = ob.binarySearch(arr=[1,2,3,4,6], N=5, K=6)
ans2 = ob.binarySearch(arr=[30, 40, 70, 85, 100], N=5, K=102)

print(ans)
print(ans2)