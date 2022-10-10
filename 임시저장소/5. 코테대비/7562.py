from collections import deque
import sys
input = sys.stdin.readline
test_case = int(input())

movin = [[1, 2], [-1, -2], [-1, 2], [1, -2], [2, 1], [-2, -1], [-2, 1], [2, -1]]

for t in range(test_case):
    q = deque()

    i = int(input())
    maps = [[0 for _ in range(i)] for i_ in range(i)]
    ii, jj = map(int, input().split())  # 출발지
    iii, jjj = map(int, input().split())    # 목표지
    
    if (ii == iii and jj == jjj):
        print(0)
        continue
    
    q.append([ii, jj])
    
    ans = 0
    
    while q:
        q_item = q.popleft()
        qx, qy = q_item[0], q_item[1]
        maps[qx][qy] += 1
        
        for mov in movin:
            x, y = mov[0], mov[1]
            
            if 0 <= qx + x < i and 0 <= qy + y < i and not maps[qx+x][qy+y]:
                maps[qx+x][qy+y] = maps[qx][qy]
                q.append([qx + x, qy + y])
            
            if x + qx == iii and y + qy == jjj: # 목표지에 도착했으면
                ans = maps[qx+x][qy+y]
                break
        if ans:
            print(ans)
            break