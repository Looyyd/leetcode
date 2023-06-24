class Solution(object):
    def longestConsecutivebad(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hashmap = {}
        set_of_nums = set()

        for num in nums:
            set_of_nums.add(num)
            hashmap[num]=True

        max_sequence = 0
        for num in set_of_nums:
            cur_sequence = 1
            above = num +1
            while above in hashmap:
                cur_sequence += 1
                #set_of_nums.remove(above)
                above+=1

            below = num -1
            while below in hashmap:
                cur_sequence += 1
                #set_of_nums.remove(below)
                below-=1

            if cur_sequence > max_sequence:
                max_sequence = cur_sequence

        return max_sequence

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hashmap = {}
        set_of_nums = set(nums)

        for num in set_of_nums:
            hashmap[num] = True

        max_sequence = 0

        for num in set_of_nums:
            # This important improvement makes sure that sequences are checked only once
            # we only check from the first element
            if num - 1 not in hashmap:  # Start of a sequence
                cur_num = num
                cur_sequence = 1

                while cur_num + 1 in hashmap:  # Continue the sequence
                    cur_num += 1
                    cur_sequence += 1

                max_sequence = max(max_sequence, cur_sequence)

        return max_sequence

