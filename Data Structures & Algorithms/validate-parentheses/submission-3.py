class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {"]":"[", "}":"{", ")":"("}
        stack = []

        for char in s: 

            if stack and char in bracket:
                curr = stack.pop()
                if curr != bracket[char]: 
                    return False
            else: 
                stack.append(char)
        return not stack

        