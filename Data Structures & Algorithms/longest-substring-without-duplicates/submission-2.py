class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 1
        current = 1
        lb = 0
        ub = 1

        if (len(s) == 0):
            return 0

        seen = set()
        seen.add(s[lb])
        while (ub < len(s)):
            while (s[ub] in seen):
                seen.remove(s[lb])
                lb += 1
                current -= 1
            seen.add(s[ub])
            ub += 1
            current += 1
            if (current > longest):
                longest = current
        return longest

