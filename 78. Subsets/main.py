class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sets = [[]]

        for num in nums:
            new_subsets = []
            for subset in sets:
                new_subset = subset.copy()  # Create a copy of the subset
                new_subset.append(num)
                new_subsets.append(new_subset)
            sets.extend(new_subsets)  # Use extend to add the new subsets to the original list
        return sets



nums = [1,2,3]
s = Solution()
print(s.subsets(nums))