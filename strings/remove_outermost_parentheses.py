'''
A valid parentheses string is either empty "", "(" + A + ")", or A + B, 

where A and B are valid parentheses strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string s is primitive if it is nonempty, 

and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, 

where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.
'''


class Solution:
    def removeOuterParentheses(self, s):

        '''
        approach: use a stack to keep track of outermost () pairs
        Time: O(n)
        Space: O(n)
        '''
        # code here

        st = []
        ans = ""

        # for each character in string
        for c in s:
            
            # if stack is not empty
            if st:
                ans += c

            if c == '(':
                st.append(c)
            else:
                st.pop()
                
                # if stack empty after popping element in outerpair match from the stack
                if not st:
                    # delete last update to ans
                    ans = ans[:-1]

        return ans

            



ob = Solution()
ans = ob.removeOuterParentheses(s="(()())(())(()(()))")
print(ans) 