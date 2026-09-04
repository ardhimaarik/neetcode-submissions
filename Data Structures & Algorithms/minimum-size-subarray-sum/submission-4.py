class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minL = float('inf')
        cL = 0
        l = 0
        window = float('inf')

        for r in range(len(nums)): 
            curr = nums[r]
            cL += curr
            while l<=r and cL >= target: 
                window = r-l+1
                cL -= nums[l]
                l+= 1
            minL = min(minL, window)
        return minL if minL != float('inf') else 0