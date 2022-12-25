from functools import reduce
from operator import concat

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        LCS = [[0] * (len(text2)+1)] * (len(text1)+1)
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    LCS[i+1][j+1] = LCS[i][j] + 1
                else:
                    LCS[i+1][j+1] = max(LCS[i][j+1],LCS[i+1][j])
        return max(reduce(concat,LCS))
        #WRONG ANSWER