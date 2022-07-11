class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {"O": 0,"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        valid_combinations = ["IV", "IX", "XL", "XC", "CD", "CM"]
        
        number = 0
        
        if len(s) == 1:
            return roman_dict[s]
        
        for numeral in range(len(s)-1): 
            
            if s[numeral] != "O" and roman_dict[s[numeral]] < roman_dict[s[numeral + 1]]:
                
                combination = s[numeral] + s[numeral + 1]
                
                if combination in valid_combinations:
                    number += roman_dict[s[numeral + 1]] - roman_dict[s[numeral]]
                    numeral += 1
                    
                    s = s.replace(combination, "OO", 1)
            
            else:
                
                if numeral == len(s) - 2 :
                    number += roman_dict[s[numeral]] + roman_dict[s[numeral + 1]]
                    
                else:
                    number += roman_dict[s[numeral]]
        
        return number
        