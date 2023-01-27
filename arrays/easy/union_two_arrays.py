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
        # code here

        """
        using set and sorted functions in python3
        
        return sorted(set(a+b))

        """

        """
        using two pointers
        """



ob = Solution()
ans = ob.mergeArrays(a=[1,2,3,4,5],b=[2,3,4,4,5],n=5,m=5)
print(ans)