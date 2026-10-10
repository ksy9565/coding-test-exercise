from collections import deque, defaultdict

def solution(tickets):
    answer = []
    
    # c, b, a순으로 정렬
    # pop 하면 a가 먼저 반환됨 
    tickets.sort(key=lambda x: x[1], reverse=True)
    
    t = defaultdict(list)
    for key, value in tickets:
        t[key].append(value)
    
    q = deque()
    q.append("ICN")
    
    while q:
        key = q[-1]
        
        # 현재 출발지의 티켓이 남아있다면
        if t[key]:
            value = t[key].pop()
            q.append(value)
        else: # 더 이상 갈 수 없으면 경로에 추가
            answer.append(q.pop())
            
    return answer[::-1]

###
ICN ATL JFK SFO ICN SFO ATL

ICN: SFO, ATL
ATL: JFK
JFK: SFO
SFO: ICN, ATL
###