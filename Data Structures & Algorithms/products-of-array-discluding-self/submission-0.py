class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        left = 1
        for idx, num in enumerate(nums): 
            result[idx] *= left
            left *= num
        
        right = 1
        for idx in range(n-1, -1, -1):
            result[idx] *= right
            right *= nums[idx]
        
        return result
        