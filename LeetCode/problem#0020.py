class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        open_parentheses: set[str] = {"{", "[", "("}
        close_parentheses: dict[str, [str]] = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        for parenthes in s:
            if parenthes in open_parentheses:
                stack.append(parenthes)
            elif len(stack) == 0 or close_parentheses[parenthes] != stack[-1]:
                return False
            else:
                stack.pop()
        return True if len(stack) == 0 else False
