
class Solution:
    def numDecodings(self, s: str) -> int:
        def valid_encoding(n:str):
            if n[0] == '0' : return False
            return 26 >= int(n) > 0

        dp=[1]*(len(s)+2)
        for i in range(len(s)-1,-1,-1):
            one = valid_encoding(s[i])
            two = i+1 < len(s) and valid_encoding(s[i:i+2])
            if one and two:
                dp[i]= dp[i+1]+dp[i+2]
            elif one:
                dp[i]=dp[i+1]
            elif two:
                dp[i]=dp[i+2]
            else:
                dp[i]=0

        return dp[0]


if __name__ == "__main__":
    s= "06"
    sol=Solution()
    print(sol.numDecodings(s))