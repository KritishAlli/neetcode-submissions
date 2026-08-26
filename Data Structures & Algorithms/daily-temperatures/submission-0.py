class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            if len(stack) == 0 or stack[-1][0] >= temperatures[i]:
                stack.append([temperatures[i], i])
            else:
                while len(stack) != 0 and stack[-1][0] < temperatures[i]:
                    index = stack.pop(-1)[1]
                    out[index] = i - index
                stack.append([temperatures[i], i])
        return out


