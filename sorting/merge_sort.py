class Solution:
    def merge(self,arr, l, m, r): 
        """
        used to merge the 2 halves of the array. It assumes that 
        both part of the array are sorted and merges both of them
        """ 
        # code here
        list1 = arr[l:m+1]
        list2 = arr[m+1:r+1]
        
        l1 = len(list1)
        l2 = len(list2)
        
        i=j=0  # initializing left arr copy and right arr copy counters
        k = l  # initializing inplace to-be sorted array counter
               # "k" recursively needs to be initialized to the passed "l"
        
        # storing elements in the copy arrays in a sorted manner
        while i<l1  and j <l2:
            if list1[i] <= list2[j]:
                arr[k] = list1[i]
                i += 1
            else:
                arr[k] = list2[j]
                j += 1
            k+=1
            
            
        # if elements on the left half are still left
        while i < l1:
            arr[k] = list1[i]
            i += 1
            k += 1
        
        # if elements on the right half are still left
        while j < l2:
            arr[k] = list2[j]
            j += 1
            k += 1
            
        return arr
                
    def mergeSort(self,arr, l, r):
        """
        divides the array into 2 parts . l to m and m+1 to r
        """
        #code here

        if l < r:
            
            m = (l+r) // 2
            
            self.mergeSort(arr, l, m)
            
            self.mergeSort(arr, m+1, r)
            
            self.merge(arr, l, m, r)
            
        return arr




# test
ob = Solution()
ans = ob.mergeSort(arr=[9, 4, 7, 6, 3, 1, 5], l=0, r=7-1)
print(ans)