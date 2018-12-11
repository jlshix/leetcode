# https://leetcode-cn.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        t = self.triangles()
        return [next(t) for i in range(numRows)]
    
    def triangles(self):
        l = [1]
        while True:
            yield l
            l = [sum(x) for x in zip([0]+l, l+[0])]