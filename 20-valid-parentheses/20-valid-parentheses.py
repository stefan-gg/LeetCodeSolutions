class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets_dict = {"}":"{", "]":"[", ")":"("}

        bracket_arr = []
        
        for bracket in s:
            if bracket in brackets_dict.keys() and not bracket_arr:
                return False
        
            elif not bracket in brackets_dict.keys():
                bracket_arr.append(bracket)
        
            elif bracket_arr[-1] == brackets_dict[bracket]:
                bracket_arr = bracket_arr[:-1]
            
            else:
                return False
            
        if not bracket_arr:
            return True
        
        return False