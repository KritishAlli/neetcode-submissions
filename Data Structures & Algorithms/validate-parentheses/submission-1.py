class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(0, len(s)):
            cur_char = s[i]
            if (cur_char == "(" or cur_char == "{" or cur_char == "["):
                stack.append(cur_char)
            else:
                if (len(stack) == 0):
                    return False
                elif (cur_char == "}"):
                    if (stack[-1] != "{"):
                        return False
                elif (cur_char == ")"):
                    if (stack[-1] != "("):
                        return False
                elif (cur_char == "]"):
                    if (stack[-1] != "["):
                        return False
                stack.pop()
        return (len(stack) == 0)
