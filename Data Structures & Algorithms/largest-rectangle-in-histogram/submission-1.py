class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0

        for idx, h in enumerate(heights):
            si = idx
            while stack and h < stack[-1][1]: 
                prev_idx, prev_h = stack.pop()
                area = (idx - prev_idx) * prev_h
                maxarea = max(maxarea, area)
                si = prev_idx
            stack.append((si, h))
        for i, h in stack:
            maxarea = max(maxarea, (len(heights)-i)*h)
        return maxarea
        