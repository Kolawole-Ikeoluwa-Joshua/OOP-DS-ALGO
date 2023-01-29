class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def mergeArrays(self,a,b,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        

        """
        solution 1: using set and sorted functions in python
        """
        # code here
        # return sorted(set(a+b))

    
        """
        solution 2: using two pointers
        """
        # code here

        union = []
        
        # two pointers
        i = 0
        j = 0
        
        # compare elements in both arrays
        while i < n and j < m:
            if a[i] <= b [j]:
                # current size of union array
                s = len(union)
                
                # check if element to be inserted already in union array
                if s == 0 or union[s-1] != a[i]:
                    union.append(a[i])
                i += 1
                
            else:
                s = len(union)
                if s == 0 or union[s-1] != b[j]:
                    union.append(b[j])
                j += 1
                
        
        # if element left in first array after comparison
        
        while i < n:
            s = len(union)
            if union[s-1] != a[i]:
                union.append(a[i])
            i += 1
            
        #   if element left in second array after comparison
        
        while j < m:
            s = len(union)
            if union[s-1] != b[j]:
                union.append(b[j])
                
            j += 1
            
            
        return union        

        



ob = Solution()
ans = ob.mergeArrays(a=[1,2,3,4,5],b=[2,3,4,4,5],n=5,m=5)
print(ans)