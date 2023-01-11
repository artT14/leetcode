class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0: return False
        l, r = 0, len(s) - 1
        while l < r:
            if (s[l:l+2] in ["()","[]","{}"]):
                # s = s[l+2:]
                l += 2
            elif (s[l]+s[r] in ["()","[]","{}"]):
                # s = s[l+1:r-1]
                l += 1
                r -= 1
            else:
                return False
        return True