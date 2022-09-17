import sys
input = sys.stdin.readline

n = int(input())
l = int(input())

def solution(n, S):
    s_stack = [i+1 for i, s in enumerate(S[1:l]) if s == 'I']   # 0과 l에는 있어도 소용 X
    cnt = 0
    ans = 0

    for s in range(1, len(s_stack)):
        if s_stack[s] - s_stack[s-1] == 2:
            cnt+=1
        else:   # 2차이 아니라서 연속성 끊김
            cnt = 0
        
        if cnt >= n:
            ans+=1  
            
    print(ans)      
        
S = input()
solution(n, S)