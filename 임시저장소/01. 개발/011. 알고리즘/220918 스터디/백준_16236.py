import sys
input = sys.stdin.readline

N = int(input())
graph =list()   #   그래프
pos = list() #   아기상어 위치
size = 2 #  아기상어 크기
for _ in range(N):
    row = list(map(int, input().split()))
    graph.append(row)
    if 9 in row:
        pos = [_, row.index(9)]
        
        #   아기상어 위치를 0 만들어야 해당 위치 지나감
        graph[pos[0]][pos[1]] = 0   
        
dx = [0,0,1,-1]
dy = [1,-1,0,0]

ans = 0 #   상어 이동 횟수
eat = 0 #   먹은 물고기 개수

from collections import deque 
while True:
    q = deque()
    
    #   아기 상어 현재 위치와 이동 횟수
    q.append((pos[0], pos[1], 0))   
    visited = [[False] * N for _ in range(N)]
    temp = float('INF')
    fish = []
    
    while q:
        x, y, cnt = q.popleft()
        
        if cnt > temp:
            break
        
        for dd in range(4):
            nx, ny = x + dx[dd], y + dy[dd]
            
            #   벽이면 통과 불가
            if not (0<=nx<N and 0<=ny<N) :
                continue
            
            #   현재 상어 크기보다 크면 통과 불가
            if graph[nx][ny] > size :
                continue
            
            #   방문 시 통과 필요 없음
            if visited[nx][ny] :
                continue
            
            #   해당 위치에 물고기가 있고, 상어 크기보다 작을 때
            if 0 < graph[nx][ny] < size:
                fish.append((nx, ny, cnt+1))
                temp = cnt
                
            #   0 <= graph[nx][ny] < size 일 때
            visited[nx][ny] = True
            q.append((nx, ny, cnt+1))
    
    #   현재 사이즈에서 먹을 물고기가 있을 때        
    if len(fish) > 0:
        fish.sort()
        x, y, tmp = fish[0][0], fish[0][1], fish[0][2]
        ans += tmp
        eat += 1
        graph[x][y] = 0
        
        #   아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가
        if eat == size:
            size += 1
            eat = 0
            
        pos[0], pos[1] = x, y
        
    else:
        break
        
print(ans)