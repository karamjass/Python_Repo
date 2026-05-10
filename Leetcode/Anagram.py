class Solution(object):
    def isAnagram(self, s, t):
        if len(s) !=len(t): 
            return False 
        d1={}
        d2={}
        for i in s :
            if i in d1:
                d1[i]=d1[i]+1  
            else : 
                d1[i]=1 
        for j in t :
            if j in d2:
                d2[j]=d2[j]+1 
            else : 
                d2[j]=1 
        if d1==d2:
            return True 
        else : 
            return False
