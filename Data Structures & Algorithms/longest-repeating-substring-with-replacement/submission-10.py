class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxstring = 0
        l = 0
        maxF = 0
        freq = {}

        for r in range(len(s)): 
            curr = s[r]
            freq[curr] = freq.get(curr, 0) + 1
            maxF = max(maxF, freq[curr])
            window = r - l + 1
            while window - maxF > k : 
                freq[s[l]] -= 1
                l += 1
                window = r-l+1
            maxstring = max(maxstring, window)
        return maxstring
        