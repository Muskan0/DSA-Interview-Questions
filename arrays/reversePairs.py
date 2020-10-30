# https://leetcode.com/problems/reverse-pairs/

def mergesort(nums, left,right):
    if left==right:
        return 0
    mid=(left+right)//2
    m=mergesort(nums, left,mid)
    m+=mergesort(nums, mid+1, right)
    j=mid+1
    i=left
    while i<=mid and j<=right:
        if nums[i]> 2*nums[j]:
            m+=mid-i+1
            j+=1  
        else:
            i+=1
    nums[left : right + 1] = sorted(nums[left : right + 1])
    return m        

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k=mergesort(nums, 0, len(nums)-1)
        return k
