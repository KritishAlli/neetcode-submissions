class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix)
        left = 0
        right = len(matrix[0])

        goingLeft = False
        goingRight = True
        goingUp = False
        goingDown = False

        out = []

        while top < bottom and left < right:
            if goingRight:
                for col in range(left, right):
                    out.append(matrix[top][col])
                top += 1
                goingRight = False
                goingDown = True

            elif goingDown:
                for row in range(top, bottom):
                    out.append(matrix[row][right-1])
                right -= 1
                goingDown = False
                goingLeft = True

            elif goingLeft:
                for col in range(right-1, left-1, -1):
                    out.append(matrix[bottom-1][col])
                bottom -= 1
                goingLeft = False
                goingUp = True

            elif goingUp:
                for row in range(bottom-1, top-1, -1):
                    out.append(matrix[row][left])
                left += 1
                goingUp = False
                goingRight = True
        return out