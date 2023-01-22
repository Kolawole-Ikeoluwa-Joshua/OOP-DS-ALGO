class Solution:
    def bubbleSort(self, arr, n):

        # Repeatedly swap 2 adjacent elements if arr[j] > arr[j+1] 

        for i in range(0, n-1):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

        return arr


ob = Solution()
ans = ob.bubbleSort(arr=[13,46,24,52,20,9], n=6)
print(ans)