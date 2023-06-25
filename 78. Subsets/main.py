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

# using backtrack
class Solution2:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(start, path):
            # add the subset to the results
            res.append(path)

            # iterate over the remaining elements that are unused in subset.
            for i in range(start, len(nums)):
                # generate all other subsets for the current subset.
                backtrack(i + 1, path + [nums[i]])

        res = []
        backtrack(0, [])
        return res


nums = [1,2,3]
s = Solution()
print(s.subsets(nums))