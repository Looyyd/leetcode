class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        longest_string = ""

        for i in range(len(s)):
            # try with letter in center
            length = 1
            current_string = s[i]
            left = i-1
            right = i+1
            while(left>=0 and right<=len(s)-1):
                if s[left] == s[right]:
                    length+=2
                    current_string = s[left:right+1]
                    left-=1
                    right+=1
                else:
                    break
            if longest<length:
                longest=length
                longest_string=current_string

            # not on last
            if (i<len(s)-1):
                if s[i+1] == s[i]:
                    # try with 2 letters in center
                    length = 2
                    current_string = s[i:i+2]
                    left = i - 1
                    right = i + 2
                    while (left >= 0 and right <= len(s) - 1):
                        if s[left] == s[right]:
                            length += 2
                            current_string = s[left:right+1]
                            left -= 1
                            right += 1
                        else:
                            break
                    if longest < length:
                        longest = length
                        longest_string = current_string

        return longest_string

