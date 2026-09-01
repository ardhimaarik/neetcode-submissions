class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0
        visited = set()
        left = 0
        for idx, char in enumerate(s): 
            while char in visited: 
                visited.remove(s[left])
                left+=1
            visited.add(char)
            maxL = max(maxL, idx-left+1)
        return maxL