# https://leetcode-cn.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        current = 2
        even = [1, 2, 1]
        odd = [1, 1]
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return odd
        elif rowIndex == 2:
            return even
        
        while current < rowIndex:
            if not current % 2:
                odd = (current+2) * [1]
                for i in range(1, len(odd)-1):
                    if i > len(odd) // 2 + 1:
                        odd[i] = odd[len(odd)-1-i]
                    odd[i] = even[i] + even[i-1]
            else:
                even = (current+2) * [1]
                for i in range(1, len(even)-1):
                    if i >= len(even) // 2:
                        even[i] = even[len(even)-1-i]
                    even[i] = odd[i] + odd[i-1]
            current += 1
        return odd if current % 2 else even

# TODO 44ms ver ↑   48ms ↓