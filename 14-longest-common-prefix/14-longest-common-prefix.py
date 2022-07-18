class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ''
        array_index = 0
        prefix_index = 0
        
        if strs == [""]:
            return ''
        
        if len(strs) == 1:
            return strs[0]
        
        while True:
            for string in strs:
                
                if lcp in string[0:prefix_index]:
                    array_index += 1
                
                else:
                    return lcp[0:-1]
                
                if array_index == len(strs):
                    if prefix_index >= len(strs[0]):
                        return lcp
                    
                    lcp += strs[0][prefix_index]
                    print(lcp)
                    array_index = 0
                    prefix_index += 1