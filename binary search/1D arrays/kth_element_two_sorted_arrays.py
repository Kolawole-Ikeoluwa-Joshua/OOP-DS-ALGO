'''
Given two sorted arrays arr1 and arr2 of size N and M respectively and an element K. 
The task is to find the element that would be at the kth position of the final sorted array.

'''

class Solution:
    def kthElement(self, arr1, arr2, n, m, k):

        '''
        Time: O(log(min(n,m)))
        Space: O(1)        
        '''
        # code here

        # check for smaller array to start binary search
        if n > m:
            return self.kthElement(arr2, arr1, m, n, k)
        

        low = max(0,k-m) # min elements you can take from arr1 depending on size of k: i.e if k > m (arr2 size) or not
        high = min(k, n) # max elements you can take from arr1 depending on size of k: max element will be all elements in arr1 == n
        while low <= high:
            
            # elements before k
            cut1 = (low + high) >> 1 # elements before k in arr1
            cut2 = k - cut1 # remaining element before k in arr2: = k-cut1

            # get last left elements from both left halves & # get first right elements from both right halves
            # note: out of index edge cases considered
            l1 = float('-inf') if cut1 == 0 else arr1[cut1-1]
            l2 = float('-inf') if cut2 == 0 else arr2[cut2-1]
            r1 = float('inf') if cut1 == n else arr1[cut1]
            r2 = float('inf') if cut2 == m else arr2[cut2]

            # if all elements on left half < all element right half
            if l1 <= r2 and l2 <= r1:
                return max(l1,l2) # get last elements from left halves and find max which is the kth element
            
            elif l1 > r2:
                # if smaller element in second right half.
                # remove greater element from first left half and add to first right half
                # move smaller element in second right half to second left half
                
                # to do this move left in binary search                
                high = cut1 -1

            else:
                # if smaller element in first right half. 
                # remove the greater element from second left half and add to second right half.
                # move smaller element in  in first right half to first left half
                
                # to do this move right in binary search                
                low = cut1 + 1

        return 1 # dummy return statement



ob = Solution()
ans = ob.kthElement(arr1=[2, 3, 6, 7, 9], arr2=[1, 4, 8, 10], n=5, m=4, k=5)
print(ans)