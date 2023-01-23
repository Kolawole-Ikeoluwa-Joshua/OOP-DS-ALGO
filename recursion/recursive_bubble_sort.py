class Solution:
    def recursiveBubbleSort(self, arr, n):

        # base case
        if n == 1:
            return arr


        # code
        for i in range(0, n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

        return self.recursiveBubbleSort(arr, n-1)


# test
ob = Solution()
a = [9,4,7,6,3,1,5]
length = len(a)
ans = ob.recursiveBubbleSort(arr=a, n=length)
print(ans)