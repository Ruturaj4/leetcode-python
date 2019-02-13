class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if "-" in str(x):
            x = int("-" + str(x).replace("-","")[::-1])
        else:
            x = int(str(x)[::-1])
        if abs(x) >= 2147483647:
            return 0
        else:
            return x