import ctypes

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        A =  ctypes.c_int32(a)
        B =  ctypes.c_int32(b)
        result = A.value^B.value
        carry  = (A.value&B.value) <<1 
        if carry:
            return self.getSum(result, carry)
        else:
            return result