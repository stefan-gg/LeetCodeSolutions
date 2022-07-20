class Solution:
    def mySqrt(self, x: int) -> int:
        
        # int(sqrt(x)) je isto validno
        
        for i in range(x // 2 + 1):
            if i*i <= x and (i+1)*(i+1) > x:
                return i
        
        return x