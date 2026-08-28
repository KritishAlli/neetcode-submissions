class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        maxS = 0
        curS = 0

        l = 0
        r = 0

        while r < len(s):
            if s[r] in window:
                window.remove(s[l])
                l += 1
                curS -= 1
            else:
                window.add(s[r])
                curS += 1
                maxS = max(curS, maxS)
                r += 1
        return maxS