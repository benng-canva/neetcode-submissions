class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        openParens = set(["(", "[", "{"])
        parenMap = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:
            if c in openParens:
                stack.append(c)
                continue

            if len(stack) == 0 or parenMap[c] != stack[-1]:
                return False
            
            stack.pop()

        return len(stack) == 0
        