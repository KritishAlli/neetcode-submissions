class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:

            if i == "+":
                num2 = int(stack.pop(-1))
                num1 = int(stack.pop(-1))
                stack.append(str(num1 + num2))
            elif i == "-":
                num2 = int(stack.pop(-1))
                num1 = int(stack.pop(-1))
                stack.append(str(num1 - num2))
            elif i == "*":
                num2 = int(stack.pop(-1))
                num1 = int(stack.pop(-1))
                stack.append(str(num1 * num2))
            elif i == "/":
                num2 = int(stack.pop(-1))
                num1 = int(stack.pop(-1))

                stack.append(str(int(num1 / num2)))
            else:
                stack.append(i)
        return int(stack[0])
