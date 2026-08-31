class Solution:
    def trap(self, height: List[int]) -> int:
        total_trap = 0

        left, right = 0, len(height)-1
        maxleft, maxright = 0, 0
        while left < right: 
            if height[left] < height[right]: 
                maxleft = max(maxleft, height[left])
                diff = maxleft - height[left]
                total_trap += diff
                left += 1
            else: 
                maxright = max(maxright, height[right])
                diff = maxright - height[right]
                total_trap += diff
                right -= 1
        return total_trap