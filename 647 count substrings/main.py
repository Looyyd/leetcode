class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPali(s:str)-> bool:
            for i in range(0,len(s)//2):
                if(s[i]!=s[-i]):
                    return False
            return True

        ans = 0
        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0

        if(isPali(s)):
            ans += len(s)//2
        return ans + self.countSubstrings(s[1:]) + self.countSubstrings(s[:-1])

