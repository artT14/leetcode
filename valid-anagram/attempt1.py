class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        hm = {}
        for c in s:
            if c in hm:
                hm[c] += 1
            else:
                hm[c] = 1
        for c in t:
            if c not in hm or hm[c] < 1:
                return False
            else: hm[c] -= 1
        return True
        # ACCEPTED