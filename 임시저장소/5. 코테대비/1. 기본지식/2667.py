import sys
from io import StringIO
from tokenize import String

TEST_CASE = 1
sys.stdin = StringIO(
"""7
0110100
0110101
1110101
0000111
0100000
0111110
0111000""")

from collections import deque
def solution():
    n = int(input())
    
    nmap = [[int(i) for i in input()] for _ in range(n)]
    visited = [[False for i in range(n)] for j in range(n)]
    movin = [[1,0], [0,1], [-1,0], [0,-1]]  #   상하좌우
    q = deque()
    ans_list = []
    
    for mm in range(n):
        for nn in range(n):   
            if nmap[mm][nn] and not visited[mm][nn]:
                # 단지 시작점
                ans = 0
                q.append([mm, nn])
                # print(ans)
                # print("ans_list", ans_list)
                # print("단지시작점", q)
                
                while q:                
                    pop_item = q.popleft()
                    # print("pop_item", pop_item)
                    # print(visited)
                    ans += 1
                    
                    # print(ans)
                    
                    xx, yy = pop_item[0], pop_item[1]
                    visited[xx][yy] = True
                    for mov in movin:
                        x, y = mov[0], mov[1]
                        if 0 <= x+xx < n and 0 <= y+yy < n:
                            if not visited[x+xx][y+yy] and nmap[x+xx][y+yy]:
                                q.append([x+xx, y+yy])
                                visited[xx+x][yy+y] = True
                                # print(q)
                                
                    if not q:
                        # print(ans)
                        ans_list.append(ans)
    print(len(ans_list))            # 총 단지수   
    for a in sorted(ans_list):
        print(a)
solution()