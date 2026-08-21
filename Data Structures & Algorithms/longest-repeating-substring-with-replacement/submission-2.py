class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        max_size = 0

        l = 0
        for r in range(len(s)):
            # counts.get either returns s[r] or 0 if not in hmap
            counts[s[r]] = 1 + counts.get(s[r], 0)


            while r-l+1 - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
            if r-l+1 > max_size:
                max_size = r-l+1
        return max_size

        



                