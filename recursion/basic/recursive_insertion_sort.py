class Solution:
    def recursiveInsertionSort(self, alist, n):

        # base case (when there's only 1 element to sort)

        if n == 1:
            return

        # recursively sort inner elements
        self.recursiveInsertionSort(alist, n-1)

        last = alist[n-1]
        j = n-2

        # iterate over each element in the sorted subarray to insert current element
        while j >= 0 and alist[j] > last:
            # shift elements pos by 1 to insert the current element at appropriate pos
            alist[j+1] = alist[j]
            j -= 1

        # insert current element at appropriate position
        alist[j+1] = last 

        return alist   




ob = Solution()
ans = ob.recursiveInsertionSort(alist=[13,46,24,52,20,9], n=6)
print(ans)