class Solution:
    # class to reverse an array recursively

    def reverseArray(self, a, l, r):
        if l >= r:
            return
        # swap pointer l and r on array a
        a[l], a[r] = a[r], a[l]
        self.reverseArray(a, l+1, r-1)
        return a

ob = Solution()
a=[1,3,2,5,4]

# pointer l = starts at first element in array
# pointer r =  starts at last element in array

ans = ob.reverseArray(a=[1,3,2,5,4], l=0, r=len(a)-1)

print(ans)


        

    