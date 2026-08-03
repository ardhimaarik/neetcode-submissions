class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"}":"{", "]":"[",")":"("}

        for idx, char in enumerate(s): 
            if char in brackets: 
                top_element = stack.pop() if stack else "#"
                if  top_element != brackets[char]: 
                    return False
            else: 
                stack.append(char)
        return not stack
        