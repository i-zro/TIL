import sys
from io import StringIO
from tokenize import String

TEST_CASE = 2
sys.stdin = StringIO(
"""2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
1
5 3 6
0 2
1 2
2 2
3 2
4 2
4 0""")
answer=(
"""5, 1
2"""
    )
# print(answer)

import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def solution():
    test_case = int(input())
    for t in range(test_case):
        m, n, k = map(int, input().split())
        
        farm = [deque() for _ in range(m)]
        q = deque()
        # print(farm)
        # print(visited)
        for kk in range(k):
            i, j = map(int, input().split())
            farm[i].append(j)
        
        for idx, lst in enumerate(farm):
            if lst:
                q.append([idx, lst[0]])
                break
        
        movin = [[1, 0], [0, 1], [-1,0], [0,-1]]            
        ans = 0
        
        while q:
            pop_item = q.popleft()
            if pop_item[1] in farm[pop_item[0]]:
                farm[pop_item[0]].remove(pop_item[1])
                # print(farm)
                # visited[pop_item[0]][pop_item[1]] = True
                # print(pop_item)
                for mov in movin:
                    x, y = pop_item[0] + mov[0], pop_item[1] + mov[1]
                    if 0<=x<m and 0<=y<n:
                        if y in farm[x]:
                            q.append([x, y])
                    
            # print(visited)
            if not q:
                # print(ans)
                ans += 1   
                break_point = False
                for i_f, f in enumerate(farm):
                    if f:
                        q.append([i_f, f[0]])
                        break
                        
        print(ans)
            
            
            
        
        # q = deque()
        # q.append(farm[0][0])
        # while q:
        #     print(q.popleft())

for T in range(TEST_CASE): 
    print('\033[95m'+"테스트 케이스 %d"%(T+1)+ '\033[0m')
    solution()
    print('\033[91m'+"정답"+ '\033[0m')
    print(answer.split('\n')[T])


# for _ in range(n):
#     print(input().split())
# from itertools import combinations
# from collections import deque

