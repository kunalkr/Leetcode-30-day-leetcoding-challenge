class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        final_shift = 0
        for step in shift:
            final_shift += (2 * step[0] - 1) * step[1]
        final_shift *= -1
        final_shift %= len(s)
        
        return s[final_shift:] + s[:final_shift]
