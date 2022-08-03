# 1. IOI에서 IO를 계속 제거한다?
import sys
input = sys.stdin.readline

n = int(input())
l = int(input())
S = input()

def solution(n):
    # return n
    ans = 0
    P = 'I' + 'OI' * n
    for s in range(l):
        if S[s] == "I":
            if S[s:s+len(P)] == P:
                # print(S[s:s+len(P)])
                ans+=1
                continue
    return ans
    
print(solution(n))