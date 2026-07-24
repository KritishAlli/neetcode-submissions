class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left = 0
        right = len(matrix) - 1

        while left <= right:

            mid = (left + right) // 2

            if (target >= matrix[mid][0] and (mid == len(matrix) - 1 or target < matrix[mid + 1][0])):
                return self.binarySearch(matrix[mid], target)

            elif (target < matrix[mid][0]):
                right = mid - 1
            else:
                left = mid + 1
        return False
    

    def binarySearch(self, array: List[int], target: int) -> bool:
        left = 0
        right = len(array) - 1

        while left <= right:

            mid = (left + right) // 2

            if (target == array[mid]):
                return True

            elif (target < array[mid]):
                right = mid - 1
            else:
                left = mid + 1
        return False
    