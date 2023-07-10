from k import s
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        i,j =0,0
        max_streak = 0
        k_left = k
        char_count = {}
        target_char = s[i]
        while j!= len(s):
            curr_char=s[j]

            if target_char == curr_char:
                if curr_char in char_count:
                    char_count[curr_char] += 1
                else:
                    char_count[curr_char] = 1
                j+=1
            elif k_left == 0:
                # account for streak (it comes from previous window so j-1
                max_streak = max(max_streak, (j-1) - i + 1)
                #slide
                char_count[s[i]] -=1
                i = i +1

                # look for new target
                max_count = 0
                max_key = curr_char
                if curr_char in char_count:
                    char_count[curr_char] += 1
                else:
                    char_count[curr_char] = 1
                for key,value in char_count.items():
                    if value>max_count:
                        max_key=key
                        max_count=value
                target_char = max_key
                # number of chars - target_chars
                k_left = (j - i) + 1 - max_count
            else:
                if curr_char in char_count:
                    char_count[curr_char] += 1
                else:
                    char_count[curr_char] = 1
                k_left -=1
                j+=1
        # if have some k_left, heck if can't go back
        # could happen if we end on a character streak
        # ex: AABBBB
        i=i-1# trying previous characters
        j-=1#because we just overflew
        while k_left>0 and i>=0:
            if s[i] == target_char:
                i-=1
            else:
                k_left -=1
                i-=1

        max_streak = max(j - (i+1) + 1,max_streak)
        return max_streak


k = 2666
sol = Solution()
k=0
s="BAAA"
print(s)

print(sol.characterReplacement(s,k ))


