class Solution:

    def encode(self, strs: List[str]) -> str:
        outstr = ""
        for i in strs:
            outstr += str(len(i)) +  "~"
            outstr += i
        return outstr


    def decode(self, s: str) -> List[str]:

        out = []
        index = 0

        while index < len(s):
            lenstr = ""
            while s[index] != "~":
                lenstr += s[index]
                index += 1

            curlen = int(lenstr)

            curstr = ""
            index += 1
            while curlen > 0:

                curstr += s[index]
                index += 1
                curlen -= 1
            out.append(curstr)
        return out



