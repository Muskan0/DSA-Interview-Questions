# https://practice.geeksforgeeks.org/problems/implement-atoi/1#

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,string):
        flag=0
        ind=0
        if string[0]=='-':
            flag=1
            ind=1
        ans=0
        for i in string[ind:]:
            k=ord(i)
            if k>=48 and k<=57:
                # ASCII of '0' is 48
                ans=ans*10+(k-48)
            else:
                return -1
        if flag==1:
            ans=-1*ans
        return ans
    # time complexity= O(n)
    # space complexity= O(1)
