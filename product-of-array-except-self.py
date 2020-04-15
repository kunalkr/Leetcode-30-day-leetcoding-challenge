class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [1]*N
        
        # [1, 2, 3, 4]
        # [1, 1, 2, 6]
        # [1, 12, 8, 6]
        
        for i in range(1, N):
            res[i] = nums[i-1]*res[i-1]

        temp = 1
        for i in range(N-1, -1, -1):
            res[i] *= temp
            temp *= nums[i]
    
        return res
        
#         N = len(nums)
#         res = [1] * N

#         temp = 1

#         for i in range(N):
#             res[i] = temp
#             temp *= nums[i]

#         temp = 1

#         for i in range(N-1, -1, -1):
#             res[i] *= temp
#             temp *= nums[i]

#         return res
