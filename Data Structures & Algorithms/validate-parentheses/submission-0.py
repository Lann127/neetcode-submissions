class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cart = {"}":'{',']':'[',')':'('}
        for char in s:
            if char in cart:
                if stack and stack[-1] == cart[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack
