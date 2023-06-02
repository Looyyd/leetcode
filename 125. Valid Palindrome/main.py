class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def search_letter(begin_pointer, end_pointer):
            while not s[begin_pointer].isalnum():
                begin_pointer+=1
                if begin_pointer>end_pointer:
                    # no more valid character, we can end
                    return 0,0
            while not s[end_pointer].isalnum():
                end_pointer-=1
                if end_pointer< begin_pointer:
                    return 0,0
            return  begin_pointer, end_pointer

        begin_pointer= 0
        end_pointer=len(s) -1

        while 1:
            begin_pointer, end_pointer = search_letter(begin_pointer, end_pointer)
            a =  s[begin_pointer].lower()
            b = s[end_pointer].lower()

            if a != b:
                return False
            else:
                # if we are at the same spot or less, we are done,
                begin_pointer +=1
                end_pointer -=1
                if begin_pointer >= end_pointer:
                    return True




if __name__ == "__main__":
    print(0*10)

