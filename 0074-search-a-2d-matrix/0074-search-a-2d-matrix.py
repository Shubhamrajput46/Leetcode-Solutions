class Solution(object):
    def searchMatrix(self, matrix, target):
        rows=len(matrix)
        cols=len(matrix[0])

        l=0  # frst index
        r=rows*cols-1  #last index 

        while l<=r:
            mid=(l+r)//2
            

            if matrix[mid//cols][mid%cols]==target:
                return True
            elif matrix[mid//cols][mid%cols]>target:
                r = mid -1
            else:
                l=mid+1
        return False       
                 
        