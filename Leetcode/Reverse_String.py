class Solution(object):
    def reverseString(self, s):
        S=list(s)
        s[:]= S[::-1]
        return s