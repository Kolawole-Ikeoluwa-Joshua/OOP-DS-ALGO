class Solution:
    def merge(self, arr, l, m, r):
        i = l

        """use a temporary array to store elements in sorted order from divided arrays.
           return back the elements in the original array from temp array."""

        temp = [0] * 100000

        i = l # starting index of left half of arr
        j = m + 1;   # starting index of right half of arr
        f = l ;        # index used to transfer elements in temporary array


        # storing elements in the temporary array in a sorted manner

        while i <= m and j <= r:
            if arr[i] < arr[j]:
                temp[f] = arr[i]
                i+= 1
            
            else:
                temp[f] = arr[j]
                j += 1

            f += 1

        # if elements on the left half are still left

        if i > m:
            while j <= r:
                temp[f] = arr[j]
                f += 1
                j += 1
        
        # if elements on the right half are still left
        else:

            while i <= m:
                temp[f] = arr[i]
                f += 1
                i += 1


        # transfering all elements from temp to arr

        for f in range(l, r+1):
            arr[f] = temp[f]

        

    # Divide the array around the middle element by making the recursive call
    def mergeSort(self, arr, l, r):
        if l < r:
            m = (l+r)//2

            # left half
            self.mergeSort(arr, l, m)
            # right half
            self.mergeSort(arr, m+1, r)

            # merge sorted halves
            self.merge(arr, l, m, r)
            
        return arr



# test
ob = Solution()
ans = ob.mergeSort(arr=[9, 4, 7, 6, 3, 1, 5], l=0, r=7-1)
print(ans)