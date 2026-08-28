class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(["{}#{}".format(len(s),s) for s in strs])

    def decode(self, s: str) -> List[str]:
        result = []
        left = 0
        while left < len(s): 
            right = left
            while s[right] != "#": 
                right += 1
            
            num = int(s[left:right])
            word = s[right + 1: right + 1 + num]
            left = right + 1 + num
            result.append(word)
        return result