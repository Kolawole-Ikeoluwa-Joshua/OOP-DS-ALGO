class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def intersectArrays(self,a,b,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The intersection of both arrays as a list
        '''
    
        """
        using two pointers
        """
        # code here

        intersect = []
        
        # two pointers
        i = 0
        j = 0
        
        # traverse arrays and compare elements in first array to second array elements
        while i < n and j < m:
            
            # if current element i in first array is smaller, go to next element
            if a[i] < b[j]:
                i += 1
            
            # if current element j in second array is smaller, go to next element
            elif b[j] < a[i]:
                j += 1

            # both elements are equal
            else:
                intersect.append(a[i])
                i += 1
                j += 1

        return intersect

  

        
ob = Solution()
ans = ob.intersectArrays(a=[1,2,3,4,5],b=[2,3,4,4,5],n=5,m=5)
print(ans)