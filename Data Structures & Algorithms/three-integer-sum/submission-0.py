class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                lpointer = i+1
                rpointer = len(nums) - 1

                while lpointer < rpointer:
                    totsum = nums[i] + nums[lpointer] + nums[rpointer]
                    if totsum > 0:
                        rpointer -= 1
                    elif totsum < 0:
                        lpointer += 1
                    else:
                        out.append([nums[i], nums[lpointer], nums[rpointer]])
                        lpointer += 1
                        while lpointer < rpointer and nums[lpointer] == nums[lpointer-1]:
                            lpointer += 1

                    

        return out
