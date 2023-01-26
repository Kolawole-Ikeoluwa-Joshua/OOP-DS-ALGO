class Solution:
    def arraySortedOrNot(self, arr, n):
        # code
        # this takes 0.17 sec

        for i in range(0, n-1):
            if arr[i] > arr[i+1]:
                return False
                
                
        return True

        """
        # this solution takes 0.19 sec

        prev = arr[0]
        
        for i in range(1, n):
            if arr[i] < prev:
                
                return False
                
            elif arr[i] == prev:
                prev = arr[i]
                
            else:
                prev = arr[i]
                
        return True"""        



ob = Solution()
ans = ob.arraySortedOrNot(arr=[1,4,16,50,88,100,101], n=7)
ans2 = ob.arraySortedOrNot(arr=[90, 80, 100, 70, 40, 30], n=6)
print(ans)
print(ans2)