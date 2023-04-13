class Solution:

	def reverser(self, S):
		ans = ""
        
		length = len(S)
        
		while length > 0:
			ans += S[length-1]
			length -= 1
		return ans
            
	def isPalindrome(self, S):
		# code here
		
		length = len(S)

		if length == 1:
			return 1
		
		if self.reverser(S) == S:
			return 1
		else:
			return 0


ob = Solution()
ans = ob.isPalindrome(S="abbbc")

print(ans)