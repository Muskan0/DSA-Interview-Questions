# https://practice.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1#

class Solution:
    def median(self, matrix, r, c):
    	min1=9999
    	max1=0
    	for i in range(r):
    	    for j in range(c):
    	        min1=min(min1, matrix[i][j])
    	        max1=max(max1, matrix[i][j])
    	low=min1
    	high=max1
    	while low<=high:
    	    mid=(low+high)//2
    	    count=0
    	    for i in range(r):
    	        count+=smallerthanmid(matrix[i],mid, c)
    	    if count <= (r*c)//2:
    	        low=mid+1
    	    else:
    	        high=mid-1
        return low
      
def smallerthanmid(row, middle, r):
    low=0
    high=r-1
    while low<=high:
        mid=(low+high)//2
        if row[mid]<=middle: #smaller than equal to
            low=mid+1
        else:
            high=mid-1
    return low
  
'''
Time complexity: log2(k) * N * log2(M),
where k is the difference between minimum and maximum element of array at 
max it can be 32, so log2(@^32)=32
So, it is O(32*r*log2(c))
Space Complexity: O(c), for passing the array to the function which can
further be reduced to O(1)
'''
