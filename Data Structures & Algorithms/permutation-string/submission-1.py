class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m1 = {}
        m2 = {}
        if len(s2) < len(s1):
            return False
        for i in range(len(s1)):
            m1[s1[i]] = 1 + m1.get(s1[i], 0)
        l = 0
        r = 0
        k = len(s1)
        for r in range(0, k):
            m2[s2[r]] = 1 + m2.get(s2[r], 0)


        while r < len(s2):
            if m1 == m2:
                return True
            
            m2[s2[l]] -= 1
            if m2[s2[l]] == 0:
                del m2[s2[l]]
            l += 1
            r += 1
            if r < len(s2):
                m2[s2[r]] = 1 + m2.get(s2[r], 0)
        return False

            

            