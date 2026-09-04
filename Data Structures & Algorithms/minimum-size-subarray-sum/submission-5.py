class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cL = 0
        l = 0
        window = float('inf')

        for r in range(len(nums)): 
            curr = nums[r]
            cL += curr
            while l<=r and cL >= target: 
                window = min(r-l+1, window)
                cL -= nums[l]
                l+= 1
        return window if window != float('inf') else 0