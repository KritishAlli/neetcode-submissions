class Solution:
    def findMinRec(self, a1: List[int], a2: List[int]):
        if (a1[0] < a2[-1]):
            return a1[0]
        if (len(a2) == 1):
            if a1[0] < a2[0]:
                return a1[0]
            else:
                return a2[0]
        elif (len(a2) == 2 and len(a1) == 1):
            if (a1[0] > a2[0]):
                return a2[0]
            elif (a1[0] > a2[1]):
                return a2[1]
            else:
                return a1[0]
        selected_arr = a2
        if (a1[0] > a1[-1]):
            selected_arr = a1

        arr1 = selected_arr[0:len(selected_arr)//2]
        arr2 = selected_arr[len(selected_arr)//2:len(selected_arr)]

        return self.findMinRec(arr1, arr2)

    def findMin(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return nums[0]

        arr1 = nums[0:len(nums)//2]
        arr2 = nums[len(nums)//2:len(nums)]

        return self.findMinRec(arr1, arr2)