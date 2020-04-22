# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        res = -1
        R, C = binaryMatrix.dimensions()
        r, c = 0, C-1
        
        while r < R and c >= 0:
            # Retrieve bit value
            bit = binaryMatrix.get(r, c)
            if bit == 0:
                # Going down
                r += 1
            else:
                # update leftmost column with 1 index
                res = c
                # Going left
                c -= 1
        return res
