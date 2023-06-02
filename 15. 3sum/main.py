"""
This solution works but is not optimal, the optimal uses left and right pointers to solve the two sum(once the
first number is fixed)
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        p1 = 0
        p2 = 1
        maxPointer = len(nums) -1

        tested_n1 = []
        tested_n2 = []

        triplets = []

        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i


        while 1:
            n1 = nums[p1]
            n2 = nums[p2]

            if not n1 in tested_n1:
                if not n2 in tested_n2:
                    n3 = -(n1 + n2)
                    if n3 in hashmap:
                        p3 = hashmap[n3]
                        # only append if we are to the right, otherwise duplicates happen
                        if p3 > p2:
                            triplets.append([n1, n2, n3])

            if p1 == maxPointer - 2:
                return triplets
            else:
                if p2 == maxPointer - 1:
                    tested_n1.append(n1)
                    # since we are starting with a new p3, we have to retest all
                    tested_n2 = []
                    p1 += 1
                    p2 = p1 + 1
                else:
                    tested_n2.append(n2)
                    p2 = p2 + 1


if __name__ == "__main__":
    nums = [0,0,0]
    s = Solution()
    print(s.threeSum(nums))
