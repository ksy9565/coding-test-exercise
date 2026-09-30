class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        # 뒤집어도 똑같으면 찾을 필요가 없다 ~
        if s == s[::-1]:
            return len(s)

        ### Bottom-up 방식
        ##########################################
        # n = len(s) # 문자열 s의 길이

        # # dp[i][j] = 구간 [i, j]에 대해 최장 회문 문자열 길이 저장 <= n
        # dp = [[0]*n for _ in range(n)]
        # # [[0, 0, ..., 0],
        # #  [0, 0, ..., 0]
        # #  ...
        # #  [0, 0, ..., 0]]

        # # 길이가 1이면 항상 회문임.
        # for i in range(n):
        #     dp[i][i] = 1

        # for length in range(2, n+1):
        #     for left in range(n - length + 1):
        #         right = left + length - 1
                
        #         if s[left] == s[right]: # 회문 조건 만족 시
        #             dp[left][right] = dp[left+1][right-1] + 2 # 사이 구간에 문자 개수 2 추가
        #         else:
        #             dp[left][right] = max(dp[left+1][right], dp[left][right-1]) # 아니면 그대로
        
        # return dp[0][n-1]
        ##########################################

        ### Top-down 방식
        ##########################################
        n = len(s) # 문자열 s의 길이
        memo = {} # 딕셔너리: 키-값 쌍을 저장. key=구간, value=길이

        def solve(left, right):
            if left > right:
                return 0
            if left == right:
                return 1
            if (left, right) in memo:
                return memo[(left, right)] # 저장된 값을 반환

            if s[left] == s[right]:
                result = solve(left+1, right-1) + 2 # 더 작은 구간으로 함수 재귀호출
            else:
                result = max(solve(left+1, right), solve(left, right-1))
            
            memo[(left, right)] = result
            return result

        return solve(0, n-1)
        ##########################################