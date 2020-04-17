class Solution:
    def checkValidString(self, s: str) -> bool:
        N = len(s)
        forwardParseCount = backwardParseCount = 0

        for i in range(N):
            if s[i] in {'(', '*'}:
                forwardParseCount += 1
            else:
                forwardParseCount -= 1

            if s[N - 1 - i] in {')', '*'}:
                backwardParseCount += 1
            else:
                backwardParseCount -= 1
            
            if forwardParseCount < 0 or backwardParseCount < 0:
                return False
        return True
