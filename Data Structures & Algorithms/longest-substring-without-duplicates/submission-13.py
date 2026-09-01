class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0
        visited = {}
        left = 0
        for idx, char in enumerate(s):
            if char in visited: 
                left = max(visited[char]+1, left)
            visited[char] = idx
            maxL = max(maxL, idx-left+1) 
            # while char in visited: 
            #     visited.remove(s[left])
            #     left+=1
            # visited.add(char)
            # maxL = max(maxL, idx-left+1)
        return maxL