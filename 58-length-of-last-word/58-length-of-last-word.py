class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")
        while s[-1] == "":
            s = s[:-1]
        return len(s[-1])