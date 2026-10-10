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

        # # 길이가 1이면 항상 회문임. 얘는 길이 1
        # for i in range(n):
        #     dp[i][i] = 1

        # # length = 문자열 기준 길이: 문자열 길이가 3개일때, 무조건 길이 2에 대한 모든 결과를 미리 계산
        # # 나는 길이 2에대한 걸 모두 계산하고 3으로 넘어가지만
        # # 필요한 구간만 계산을 한다는 느낌
        # # 길이 3을 계산하기 위해 필요한 길이 2 결과만 딱딱 먼저 계산하는 느낌
        # for length in range(2, n+1): # 길이 2일때부터 계산.
        #     for left in range(2): # n=5, length=4 -> left =  0,1밖에안됨 for문 조건이 for(int left = 0; left < 3; left++)
        #         right = left + length - 1 #                       right= 3
                
        #         if s[left] == s[right]: # 회문 조건 만족 시
        #             dp[left][right] = dp[left+1][right-1] + 2 # 사이 구간에 문자 개수 2 추가
        #         else:
        #             dp[left][right] = max(dp[left+1][right], dp[left][right-1]) # 아니면 그대로
        
        # return dp[0][n-1]
        ##########################################

        ### Top-down 방식 - Bottom-up 방식에서는 dp 배열 자체가 이미 이전 결과를 저장해주지만
        # top-down에서는 재귀를 쓰기 때문에, 이전 결과를 저장해주는 배열이 따로 필요하다.
        # 메모이제이션 이라고 하더라.
        ##########################################
        n = len(s) # 문자열 s의 길이
        memo = {} # map: 키-값 쌍을 저장. key=구간, value=길이

        def solve(left, right):
            if left > right:
                return 0
            if left == right:
                return 1
            if (left, right) in memo: # 이미 계산된 적 있는 값이면
                return memo[(left, right)] # 저장된 값을 반환

            if s[left] == s[right]:
                result = solve(left+1, right-1) + 2 # 더 작은 구간으로 함수 재귀호출
            else:
                result = max(solve(left+1, right), solve(left, right-1))
            
            memo[(left, right)] = result # result: 결과 길이, memo에다가 저장한다. << 메모이제이션
            return result

        return solve(0, n-1)
        ##########################################