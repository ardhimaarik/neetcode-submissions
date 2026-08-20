class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for val in tokens: 
            if val == "+": 
                stack.append(stack.pop()+stack.pop())
            elif val == "-": 
                right = stack.pop()
                left = stack.pop()
                stack.append(left-right)
            elif val == "*": 
                stack.append(stack.pop()*stack.pop())
            elif val == "/": 
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left/right))
            else : 
                stack.append(int(val))
        return stack[0]

        