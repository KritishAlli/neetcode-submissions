class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        max_size = 0
        maxf = 0

        l = 0
        for r in range(len(s)):
            # counts.get either returns s[r] or 0 if not in hmap
            counts[s[r]] = 1 + counts.get(s[r], 0)
            if counts[s[r]] > maxf:
                maxf = counts[s[r]]


            while r-l+1 - maxf > k:
                counts[s[l]] -= 1
                if counts[s[l]] == maxf-1:
                    maxf = max(counts.values())
                l += 1

            if r-l+1 > max_size:
                max_size = r-l+1
        return max_size

        



                