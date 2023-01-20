class Solution: 
    
    def selectionSort(self, arr,n):
        #code here
        
        for i in range(0, n-1):
            mini = i
            for j in range(i+1, n):
                if arr[j] < arr[mini]:
                    mini = j
                
        
            arr[mini], arr[i] = arr[i], arr[mini]
        return arr


ob = Solution()
ans = ob.selectionSort(arr=[4,1,3,9,7], n=5)
print(ans)