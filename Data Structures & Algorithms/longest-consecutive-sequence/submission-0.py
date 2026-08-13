class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxcount = 0
        curcount = 0
        for i in numset:
            if i-1 not in numset:
                curcount = 1
                val = i
                while val+1 in numset:
                    curcount += 1
                    val += 1

                if curcount > maxcount:
                    maxcount = curcount
                curcount = 1
        return maxcount
