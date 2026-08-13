class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1] * len(nums)
        curprod = nums[0]
        for i in range(1, len(nums)):
            out[i] = curprod
            curprod *= nums[i]
        curprod = nums[len(nums)-1]
        for i in range(len(nums)-2, -1, -1):
            out[i] *= curprod
            curprod *= nums[i]
        return out


