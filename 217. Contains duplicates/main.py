class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        hash_table = {}
        for n in nums:
            if n in hash_table:
                return True
            else:
                hash_table[n]=True
        return False


if __name__ == "__main__":
    nums= [1,1,1,3,3,4,3,2,4,2]
    s = Solution()
    print(s.containsDuplicate(nums))