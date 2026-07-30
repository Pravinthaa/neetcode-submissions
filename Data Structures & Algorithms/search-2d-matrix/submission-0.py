class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=len(matrix)
        c=len(matrix[0])
        top=0
        bottom=len(matrix)-1
        while top<=bottom:
            mid=(top+bottom)//2
            if target<matrix[mid][0]:
                bottom=mid-1
            elif target>matrix[mid][c-1]:
                top=mid+1
            else:
                break
            
        if not(top<=bottom):
            return False
        row=(top+bottom)//2
        left=0
        right=c-1
        while left<=right:
            mid=(left+right)//2
            if matrix[row][mid]==target:
                return True
            elif target<matrix[row][mid]:
                right=mid-1
            else:
                left=mid+1
        return False

        