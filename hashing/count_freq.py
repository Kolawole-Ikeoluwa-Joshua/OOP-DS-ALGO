class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        # code here
        a = max(N, P)
        arr1 = [0]*(a+1)
        
        
        
        for i in arr:
            arr1[i] += 1
            
        
        for i in range(N):
            arr[i] = arr1[i+1]
            
        return arr

ob = Solution()
ans = ob.frequencyCount(arr=[2,3,2,3,5], N=5, P=5)
print(ans)