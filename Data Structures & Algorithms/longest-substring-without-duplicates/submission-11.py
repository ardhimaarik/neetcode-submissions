class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlenght = 0
        left = 0
        visited = {}
        
        for right, char in enumerate(s): 
            if char in visited:
                left = max(visited[char]+1, left)
            visited[char] = right
            maxlenght = max(maxlenght, right - left + 1)

            # while s[right] in visited:
            #     visited.remove(s[left])
            #     left += 1
            # visited.add(char)
            # maxlenght = max(maxlenght, right - left + 1)
        return maxlenght