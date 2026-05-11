class Solution(object):
    def longestPalindrome(self, s):
        result = ""

        for i in range(len(s)):

            # odd palindrome
            left = i
            right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            if len(s[left+1:right]) > len(result):
                result = s[left+1:right]

            # even palindrome
            left = i
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            if len(s[left+1:right]) > len(result):
                result = s[left+1:right]

        return result