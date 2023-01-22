class Solution:
    def insertionSort(self, alist, n):

        # for each iteration get an index after the first element in the array to be sorted
        for i in range(1, n):
            index = i

            # check if every element before that index is sorted
            for j in range(index, 0, -1):

                if alist[j] < alist[j-1]:
                    alist[j], alist[j-1] = alist[j-1], alist[j]

        return alist



ob = Solution()
ans = ob.insertionSort(alist=[13,46,24,52,20,9], n=6)
print(ans)