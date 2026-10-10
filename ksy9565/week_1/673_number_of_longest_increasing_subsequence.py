class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:

        dp = [1]*len(nums) # nums[0]~nums[i]만큼의 최장 증가 수열의 길이.
        count = [1]*len(nums) # dp[i]의 길이인 서로 다른 수열의 개수

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j]+1:
                        dp[i] = dp[j]+1
                        count[i] = count[j] # 이전 최장 증가 수열의 개수
                    elif dp[i] == dp[j]+1:
                        count[i] += count[j] # 
        
        lis_len = max(dp)

        lis_idx = [i for i in range(len(nums)) if lis_len == dp[i]]
        answer = 0
        for i in lis_idx:
            answer += count[i]
            
        # answer = sum(cnt for cnt, length in zip(count, dp) if length == lis_len)
        return answer