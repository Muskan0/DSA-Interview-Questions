# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window optimized
        d=dict()
        n=len(s)
        l=r=0
        ans=0
        while r<n:
            if s[r] in d:
                l=max(d[s[r]]+1, l)
            d[s[r]]=r
            ans=max(ans,r-l+1)
            r+=1
        #print(d)
        return ans
    
        '''
        # sliding window approach
        n=len(s)
        s=list(s)
        ans=i=j=0
        st=set()
        while(i<n and j<n):
            if(s[j] not in st):
                st.add(s[j])
                j+=1
                ans=max(ans,j-i)
            else:
                st.remove(s[i])
                i+=1
        return ans
        '''
