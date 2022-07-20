class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        index = -1
        
        if digits.count(9) == len(digits):
            
            digits = [0] * (len(digits) + 1)
            digits[0] = 1
            
            return digits
        
        while digits[index] == 9:
            digits[index] = 0
            index -= 1
        
        digits[index] += 1
        
        return digits