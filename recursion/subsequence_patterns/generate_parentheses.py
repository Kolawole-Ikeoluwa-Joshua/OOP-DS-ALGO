'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''

'''
	- The idea is to add ')' only after valid '('
    - We use two integer variables left & right to see how many '(' & ')' are in the current string
    - If left < n then we can add '(' to the current string
    - If right < left then we can add ')' to the current string

'''
class Solution:

    '''
    Time: O(2^n) 
    Space: O(2^n) 
    
    '''
    def generateParenthesis(self, n):
        def dfs(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return 

            if left < n:
                dfs(left + 1, right, s + '(')

            if right < left:
                dfs(left, right + 1, s + ')')

        res = []
        dfs(0, 0, '')
        return res

# Tests

ob = Solution()
ans = ob.generateParenthesis(3)

# Output
print(ans)