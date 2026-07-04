class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for i in nums:
            if i in hmap:
                hmap[i] += 1
            else:
                hmap[i] = 1
        outlist = []
        for i in range(0, k):
            maximum = 0
            maxkey = 999
            for key, val in hmap.items():
                if val > maximum:
                    maximum = val
                    maxkey = key
            outlist.append(maxkey)    
            del hmap[maxkey]
        return outlist
