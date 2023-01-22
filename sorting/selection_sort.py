class Solution: 
    
    def selectionSort(self, arr,n):
        #code here
        
        # starting from 1st to second to the last in array
        for i in range(0, n-1):
            mini = i

            # for each iteration find the index of smallest element in the unsorted array  and select it
            for j in range(i+1, n):
                if arr[j] < arr[mini]:
                    mini = j
                
            # swap smallest element in array with element at index i where( i = 0 to n-1 )
            arr[mini], arr[i] = arr[i], arr[mini]
        return arr


ob = Solution()
ans = ob.selectionSort(arr=[4,1,3,9,7], n=5)
print(ans)