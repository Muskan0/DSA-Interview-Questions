# https://leetcode.com/problems/subsets/

'''
# iterative method
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # O((2^N)*N) time complexity, space complexity: O((2^N)*N)
        # no of subsets are 2^N
        
        # (2^N)*N are exactly the number of solutions for subsets multiplied by the number N of           #  elements to keep for each subset
        subsets=[[]] # start from empty subset in output list
        
        # at each step one takes new integer into consideration
        # and generate new subsets from the existing ones
        for ele in nums:
            k=len(subsets)
            for i in range(len(subsets)):
                curr=subsets[i]
                subsets.append(curr+[ele])
        return subsets
'''

# recursive method

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
    
        def powerset(subsets, index):
            # p[1,2,3,...,x] = p[1,2,3,...,x-1] + [x]
            if index<0:
                return [[]]
            ele=subsets[index]
            subsets=powerset(subsets,index-1)
            k=len(subsets)
            for i in range(k):
                subsets.append(subsets[i]+[ele])
            return subsets
            
        n=len(nums)
        return powerset(nums, n-1)
