import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        out = []
        hmap = {}
        cur_max = nums[0]
        for i in range(k):
            if nums[i] > cur_max:
                cur_max = nums[i]
            hmap[nums[i]] = 1 + hmap.get(nums[i], 0)
        out.append(cur_max)
        for i in range(k, len(nums)):
            
            hmap[nums[i]] = 1 + hmap.get(nums[i], 0)
            hmap[nums[i-k]] -= 1

            if hmap[nums[i-k]] == 0:
                del hmap[nums[i-k]]
            
            if nums[i] > cur_max:
                cur_max = nums[i]
            
            if nums[i-k] == cur_max:
                cur_max = max(hmap.keys())
            out.append(cur_max)
        return out




        
        