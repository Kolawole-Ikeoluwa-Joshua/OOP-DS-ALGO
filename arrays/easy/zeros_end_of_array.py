class Solution:
    def pushZerosToEnd(self, arr, n):
        # find non-zero elements
        temp = []

        for i in range(n):
            if arr[i] != 0:
                temp.append(arr[i])

        k = len(temp)
        # insert non-zero elements in arr
        for i in range(k):
            arr[i] = temp[i]

        # insert zero elements in arr
        while n > k:
            arr[n-1] = 0
            n -= 1

        return arr


# test
ob = Solution()
ans = ob.pushZerosToEnd(arr=[3, 5, 0, 0, 4], n=5)
print(ans)