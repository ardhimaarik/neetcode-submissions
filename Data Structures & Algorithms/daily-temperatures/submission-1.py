class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for idx, tmp in enumerate(temperatures): 
            while stack and tmp > stack[-1][1]: 
                i, t = stack.pop()
                result[i] = idx - i
            stack.append((idx, tmp))
        return result