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