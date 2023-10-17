from bisect import bisect_left
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        ans=1

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[j]> nums[i]:
                    dp[i]=max(dp[j]+1,dp[i])
            ans = max(ans, dp[i])
        return ans


class Solution2:
    #from leetcode solutions
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            idx = bisect_left(sub, num)
            if idx == len(sub):
                sub.append(num)
            else:
                sub[idx] = num
        return len(sub)

