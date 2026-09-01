class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlenght = 0
        left = 0
        visited = set()
        
        for right, char in enumerate(s): 
            while s[right] in visited:
                visited.remove(s[left])
                left += 1
            visited.add(char)
            maxlenght = max(maxlenght, right - left + 1)
        return maxlenght