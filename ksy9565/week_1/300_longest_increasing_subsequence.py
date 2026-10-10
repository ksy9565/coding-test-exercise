class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # ### DP 풀이: O(n^2)
        # dp = [1]*len(nums) # dp[i] = i번째 숫자까지의 가장 긴 증가 수열의 길이
        # # [0,1,2,3,4,5] -> 0~5까지의 LIS는 0~4까지의 LIS + 5를 추가 계산한 것이므로
        # # 최소 단위가 어디냐. 0~1까지의 LIS + for문을 돌면서 점차 추가하는 방식이 일반화 될 수 있는 식이다.
        # # 최소 단위에서 LIS를 계산하는 조건식 if문을 작성한 후에 for문을 돌렸습니다.

        # for i in range(1, len(nums)):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             if dp[i] < dp[j]+1:
        #                 dp[i] = dp[j] + 1

        # return max(dp)

        ### 이분 탐색 풀이(Binary Search): O(nlogn)
        def lower_bound(arr, target):
            left = 0
            right = len(arr)

            while left < right:
                mid = (left + right) // 2 # left, right가 5, 6이면 mid는 11/2의 몫인 5가 됨
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid

            return left # 값이 아니라 위치를 반환
        # [1,2,3,4,5]처럼 정렬된 배열 안에서 n개의 수를 모두 비교하는 것이 아니라
        # 반씩 범위를 줄여나가면서 대표값 하나씩만 비교하기. -> n번을 비교하는것 아니라 log n번만 비교하면 됨.
        # 일단 O(n)을 logn으로 줄일 수 있다는 장점이 있음. -> 조건, 배열이 정렬돼있어야함.
        # 정렬된 결과를 만들어서 비교한다는 방식.
        
        result = [] # 주어진 배열의 실제 값이 들어감

        for num in nums:
            idx = lower_bound(result, num) # left 반환함

            if idx == len(result): # left = right인 상태: target이 항상 더 큼
                result.append(num)
            else:                  # left가 곧 target의 좌표이므로
                result[idx] = num

        return len(result)