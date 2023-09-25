class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        cache = {}

        def _isInterLeave(i,j) -> bool:
            #check overflow
            if(len(s3) == i+j):
                return True
            if (i,j) in cache:
                return cache[(i,j)]
            else:
                if(i>=len(s1)):
                    a='\0'
                else:
                    a = s1[i]
                if(j>=len(s2)):
                    b='\0'
                else:
                    b = s2[j]
                c = s3[i+j]
                if (a == c):
                    if(b == c):
                        #both equal 2 options
                        cache[(i,j)] = _isInterLeave(i+1, j) or _isInterLeave(i, j+1)
                        return cache[(i,j)]
                    else:
                        cache[(i,j)] = _isInterLeave(i+1,j)
                        return cache[(i,j)]
                elif (b==c):
                    cache[(i,j)] = _isInterLeave(i,j+1)
                    return cache[(i, j)]
                else:
                    cache[(i, j)] = False
                    return cache[(i,j)]

        if (len(s1) + len(s2) != len(s3)):
            return False

        return _isInterLeave(0, 0)


