class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        hm1,hm2 = {},{}
        l, r = 0, len(s1)-1
        for c in s1:
            hm1[c] = 1 + hm1.get(c,0)
        for c in s2[l:r+1]:
            hm2[c] = 1 + hm2.get(c,0)
        if hm1 == hm2: return True
        l += 1
        r += 1
        while r < len(s2):
            c = s2[l-1]
            hm2[c] -= 1
            if hm2[c] == 0: del hm2[c]
            c = s2[r]
            hm2[c] = 1 + hm2.get(c,0)
            if hm1 == hm2: return True
            l += 1
            r += 1
        return False
		#ACCEPTED