class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        ans=0
        for i in range (0,n+1):   
            ans ^=i
        for j in nums : 
            ans ^=j 
        return ans 