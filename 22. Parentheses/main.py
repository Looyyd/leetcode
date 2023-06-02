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
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        patterns = ['(']

        for i in range(2*n -1):
            next_patterns = []
            for pattern in patterns:
                # if all parentheses closed, add parenthese
                n_open = pattern.count('(')
                n_closed = pattern.count(')')
                if n_open == n_closed:
                    next_patterns.append(pattern+'(')
                else:
                    if n_open<n:
                        next_patterns.append(pattern+'(')
                    next_patterns.append(pattern+')')
            patterns = next_patterns
        return patterns
