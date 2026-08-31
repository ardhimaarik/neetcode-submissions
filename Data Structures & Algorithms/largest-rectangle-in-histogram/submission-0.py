class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        stack = []

        for idx, h in enumerate(heights): 
            si = idx
            while len(stack) > 0 and h < stack[-1][1]: 
                i, ch = stack.pop()
                maxarea = max(maxarea, ((idx-i)*ch))
                si = i
            stack.append((si, h))
        
        for i, h in stack: 
            lastidx = stack[-1]
            maxarea = max(maxarea, ((len(heights) - i) * h))
        return maxarea