class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        res = 0
        freq = {}
        maxF = 0
        l =0
        for r, char in enumerate(s):
            freq[char] = freq.get(char, 0) + 1
            maxF = max(maxF, freq[char])
            while r - l + 1 - maxF > k: 
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
                