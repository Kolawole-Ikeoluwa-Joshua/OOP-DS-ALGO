class Solution:
    def print2largest(self, arr, n):

        largest = arr[0]
        sec_large = -1

        for i in range(1, n):
            if arr[i] > largest:
                sec_large = largest
                largest = arr[i]

            elif sec_large < largest and largest > arr[i] and sec_large < arr[i]:
                sec_large = arr[i]

        return sec_large



ob = Solution()
ans = ob.print2largest(arr=[1,4,50,50,47,2,9], n=7)
print(ans)