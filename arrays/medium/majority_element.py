'''
Given an array A of N elements. Find the majority element in the array. 
A majority element in an array A of size N is an element that appears more than N/2 times in the array.
'''

class Solution:
    def majorityElement(self, A, N):
        # Solution 1
        '''use hash table, Time: O(n), Space: O(n)

        freq = {}
        
            
        for item in A:
            if item in freq:
                freq[item] += 1
                
            else:
                freq[item] = 1
                
                
        major = N // 2
        
        for item in freq:
            if freq[item] > major:
                return item
        return -1 
        '''


        # Solution 2
        # using Boyer-Moore Voting Algorithm

        '''

        Essentially, what Boyer-Moore does is look for a suffix (suf) of array where suf[0] is the majority element in that suffix.
        To do this, we maintain a count, which is incremented whenever 
        we see an instance of our current candidate for majority element and decremented whenever we see anything else. 
        Whenever count equals 0, we effectively forget about everything in the array up to the current index 
        and consider the current number as the candidate for majority element.

        Time: O(n)
        Space: O(1)
        
        '''
        count = 0
        candidate = None

        for num in A:
            if count == 0:
                candidate = num

            count += (1 if num == candidate else -1)

        return candidate




ob = Solution()
ans = ob.majorityElement(A=[3,1,3,3,2], N=5)
print(ans)