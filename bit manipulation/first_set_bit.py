# https://practice.geeksforgeeks.org/problems/find-first-set-bit-1587115620/1#

import math
class Solution:
    
    #Function to find position of first set bit in the given number.
    def getFirstSetBit(self,n):
        if n==0:
            return 0
        # k is the two's complement of a number
        k=~(n-1)
        
        # for finding the first set bit of a number
        ans=n&k
        
        # position of the set bit
        return int(math.log2(ans))+1

# Time Complexity: O(1)
# Space Complexity: O(1)
