class Solution:
    def letterCombinations(self, digits: str):
        total_combinations = 1
        count = [0, 0, 0, 0]
        solution = []
        cc = []    
        
        dict_ = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        if digits == "":
            return []
        
        if len(digits) == 1:
            return dict_[digits]
        
        for number in digits :
            total_combinations *= len(dict_[number])

        str_len = len(digits)
        count = count[0:str_len]
        cc.append(count[:])
        #while len(solution) != total_combinations:
        for i in range(total_combinations):        


            # combination = ""
            # print(count)
            # for number in range(str_len):

            #     combination += dict_[digits[number]][count[number]]

            # solution.append(combination)
            for c in range(len(count)-1, 0, -1):    
                if count[c] == len(dict_[digits[c]])-1:

                    if c == 0:
                        if count[0] < len(dict_[digits[c]]):

                            count[0] += 1
                            for i in range(1, str_len+1):
                                count[i] = 0

                    else:
                        count[c] = 0
                        count[c-1] += 1
                else:
                    count[c] += 1

                for i in range(2):  
                    for c in range(str_len):
                        if count[c] >= len(dict_[digits[c]]):
                            count[c-1] += 1
                            count[c] = 0
                if not count[0] >= len(dict_[digits[0]]):
                    cc.append(count[:])

                if len(solution) == total_combinations:
                    break


        for c in cc:
            combination = ""
            for number in range(len(c)):
                combination += dict_[digits[number]][c[number]]
            solution.append(combination)

        return sorted(set(solution))