class Solution(object):
    def subtractProductAndSum(self, n):
        temp=n
        add=0
        product=1
        while temp>0:
            r = temp %10
            temp //=10
            add +=r
            product *=r
        return product-add
            
        