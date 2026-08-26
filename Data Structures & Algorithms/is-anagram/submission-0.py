class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        left, right = 0, len(s)
        visited = {}
        for char in s: 
            if char in visited: 
                visited[char] = visited[char]+ 1
            else: 
                visited[char] = 1
        visited2 = {}
        for char in t: 
            if char in visited2: 
                visited2[char] = visited2[char]+ 1
            else: 
                visited2[char] = 1
        if visited == visited2: 
            return True
        return False
        