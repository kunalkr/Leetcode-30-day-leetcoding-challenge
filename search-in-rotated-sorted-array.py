class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(nums, start, end, target):
            if start > end:
                return -1
            mid = start + (end - start)//2
            
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                return binarySearch(nums, start, mid-1, target)
            return binarySearch(nums, mid+1, end, target)
            
        def searchPivot(nums, start, end):
            if start > end:
                return -1
            if start ==  end:
                return start
            mid = start + (end - start)//2
            
            if mid < end and nums[mid] > nums[mid+1]:
                return mid
            if mid > start and nums[mid] < nums[mid-1]:
                return mid-1
            if nums[start] >= nums[mid]:
                return searchPivot(nums, start, mid-1)
            return searchPivot(nums, mid+1, end)
        
        N = len(nums)
        pivot = searchPivot(nums, 0, N-1)
        
        if pivot == -1:
            return binarySearch(nums, 0, N-1, target)
        if target == nums[pivot]:
            return pivot
        if target < nums[0]:
            return binarySearch(nums, pivot+1, N-1, target)
        return binarySearch(nums, 0, pivot-1, target)
