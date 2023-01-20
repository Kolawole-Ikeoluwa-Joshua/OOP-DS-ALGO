class Solution:

    def Fibb(self, n):
                
        if n <= 1:
            return n

        
        return self.Fibb(n-1) + self.Fibb(n-2)

    def printFibb(self, N):
        ans = []
        i = 1

        for i in range(1, N+1):
            ans.append(self.Fibb(i))

        return ans

        

ob = Solution()
ans = ob.printFibb(6)

print(ans)