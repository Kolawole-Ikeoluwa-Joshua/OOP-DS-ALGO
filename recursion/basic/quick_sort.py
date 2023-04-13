class Solution:
    # using Lomuto Partition
    def quickSort(self, arr, low, high):
        if low < high:

            p = self.partition(arr, low, high) # seperates array into two sub problems

            # sort sub problem on left side of partiion
            self.quickSort(arr, low, p-1)

            # sort sub problem on right side of partiion
            self.quickSort(arr, p+1, high)
        return arr

    # partion function moves elements smaller than pivot to left
    # moves elements large than pivot to right
    def partition(self, arr, low, high):
        pivot = high
        l = low
        for i in range(low, high):
            if arr[i] < arr[pivot]:
                arr[l] , arr[i] = arr[i], arr[l]

                l += 1
        # swap pivot with arr[l] so that pivot gets its correct position
        arr[l], arr[pivot] = arr[pivot], arr[l]

        # return partition
        return l



# test
ob = Solution()
a = [9,4,7,6,3,1,5]
length = len(a)
ans = ob.quickSort(arr=a, low=0, high=length-1)
print(ans)