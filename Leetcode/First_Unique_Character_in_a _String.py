class Solution(object):
    def firstUniqChar(self, s):
        d1 = {}

        for i in s:
            if i not in d1:
                d1[i] = 1
            else:
                d1[i] += 1

        for i in s:
            if d1[i] == 1:
                return s.index(i)
            
        return -1