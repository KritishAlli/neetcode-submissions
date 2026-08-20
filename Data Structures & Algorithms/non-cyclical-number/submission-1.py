class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        hsum = n

        while hsum != 1:
            if hsum in seen:
                return False
            seen.add(hsum)
            curstr = str(hsum)
            hsum = 0
            for i in curstr:
                hsum += int(i) * int(i)

            

        return True

