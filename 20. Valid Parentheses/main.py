class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = list(s)
        complements = {")":"(","]":"[","}":"{"}


        while 1:
            try:
                condition = stack.pop(0) == complements[stack.pop(-1)]
            except IndexError:
                break
            if condition == False:
                return False
        if len(stack)==0:
            return True
        else:
            return False