class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        current_string = ""
        longest_substring = 0
        for i, c in enumerate(s):
            if not c in current_string:
                current_string += c
            else:
                index_c = current_string.index(c)
                cur_length=len(current_string)
                if cur_length > longest_substring:
                    longest_substring = cur_length
                current_string = current_string[index_c+1:] + c

        cur_length=len(current_string)
        if cur_length > longest_substring:
            longest_substring = cur_length

        return longest_substring



