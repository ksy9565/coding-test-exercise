class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        ### DP 풀이: O(n^2)
        dp = [1]*len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j]+1:
                        dp[i] = dp[j] + 1

        return max(dp)

        ### 이분 탐색 풀이(Binary Search): O(nlogn)
        # def lower_bound(arr, target):
        #     left = 0
        #     right = len(arr)

        #     while left < right:
        #         mid = (left + right) // 2 # left, right가 5, 6이면 mid는 11/2의 몫인 5가 됨
        #         if arr[mid] < target:
        #             left = mid + 1
        #         else:
        #             right = mid

        #     return left # 값이 아니라 위치를 반환

        # result = [] # 주어진 배열의 실제 값이 들어감

        # for num in nums:
        #     idx = lower_bound(result, num) # left 반환함

        #     if idx == len(result): # left = right인 상태: target이 항상 더 큼
        #         result.append(num)
        #     else:                  # left가 곧 target의 좌표이므로
        #         result[idx] = num

        # return len(result)