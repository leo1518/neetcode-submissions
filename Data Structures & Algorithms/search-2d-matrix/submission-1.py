class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        while right >= left:
            mid = (right+left)//2
            if matrix[mid][0] <= target and matrix[mid][len(matrix[0])-1] >= target:
                left_1 = 0
                right_1 = len(matrix[0])-1
                while right_1 >= left_1:
                    mid_1 = (right_1 + left_1)//2
                    if matrix[mid][mid_1] == target:
                        return True
                    elif matrix[mid][mid_1] < target:
                        left_1 = mid_1 + 1
                    else:
                        right_1 = mid_1 - 1
                return False
            if matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][len(matrix[0])-1] < target:
                left = mid + 1
        return False
