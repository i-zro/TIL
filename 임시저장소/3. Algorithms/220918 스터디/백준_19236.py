import sys
from collections import deque
from copy import deepcopy

# 정답
ans = 0

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 물고기 번호 4X4 그래프
graph = [[0] * 4 for _ in range(4)]

# [x,y,방향] 그래프
move_graph = [[0, 0, 0] for _ in range(16)]

# 입력값 저장
for _ in range(4):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(0, 8, 2):
        graph[_][j // 2] = temp[j]
        move_graph[temp[j] - 1] = [_, j // 2, temp[j + 1] - 1]
        
q = deque()

# 상어의 [x,y,방향] 그래프
# 방향은 0,0의 위치에 있는 물고기 방향
shark = [0, 0, move_graph[graph[0][0] - 1][2]]

# 죽은 물고기의 방향은 -1 => -1인 곳은 체크하지 않기
move_graph[graph[0][0] - 1][2] = -1

# 상어가 0,0위치의 물고기를 잡아먹고 시작하므로 0,0위치의 물고기의 점수를 더해주고 시작
score = graph[0][0]

# 상어 위치 체크하기 위해 0,0을 -1로 바꾸기
graph[0][0] = -1

q.append((graph, move_graph, shark, score))

while q:
    qgraph, qmove_graph, qshark, qscore = q.popleft()

    for i in range(16):
        # 방향이 -1이라면 죽은 물고기
        if qmove_graph[i][2] == -1:
            continue
        else:
            x, y, d = qmove_graph[i]
            nx = x + dx[d]
            ny = y + dy[d]
            
            # 만약 물고기가 그래프 안 벗어나고 상어가 없는 곳으로 움직인다면
            if (0 <= nx < 4 and 0 <= ny < 4) and qgraph[nx][ny] != -1:
            	# 만약 다른 물고기가 있다면 위치 교환
                if qgraph[nx][ny] != 0:
                    temp = qgraph[nx][ny]
                    qgraph[nx][ny], qgraph[x][y] = i + 1, temp
                    qmove_graph[i][0], qmove_graph[i][1], qmove_graph[temp - 1][0], qmove_graph[temp - 1][1] = nx, ny, x, y
                # 만약 움직이려는 곳이 비어있다면 그냥 이동
                else:
                    qgraph[x][y], qgraph[nx][ny] = 0, i+1
                    qmove_graph[i][0], qmove_graph[i][1] = nx, ny

            # 못 가면 45도 방향 회전
            else:
                for _ in range(1, 8):
                    d = (d + 1) % 8
                    nx = x + dx[d]
                    ny = y + dy[d]
                    # 이동할 수 있는 경우
                    if (0 <= nx < 4 and 0 <= ny < 4) and qgraph[nx][ny] != -1:
                        if qgraph[nx][ny] != 0:
                            temp = qgraph[nx][ny]
                            qgraph[nx][ny], qgraph[x][y] = i + 1, temp
                            qmove_graph[i][0], qmove_graph[i][1], qmove_graph[temp - 1][0], qmove_graph[temp - 1][1] = nx, ny, x, y
                            qmove_graph[i][2] = d
                        else:
                            qgraph[x][y], qgraph[nx][ny] = 0, i+1
                            qmove_graph[i][0], qmove_graph[i][1] = nx, ny
                            qmove_graph[i][2] = d
                        # 이동을 했으면 break문 써서 방향 바꾸기 멈추기
                        break
    # 상어 위치, 방향
    sx, sy, sd = qshark
    # 상어 움직였는지 여부
    flag = True
    # 상어는 어느 방향이든 최대 4칸까지 이동 가능
    for j in range(1, 4):
        # 상어 이동 가능 위치
        nsx, nsy = sx + dx[sd] * j, sy + dy[sd] * j
        
        # 상어가 이동 가능 하다면
        if 0 <= nsx < 4 and 0 <= nsy < 4 and qgraph[nsx][nsy] > 0:
            
            # deepcopy로 기존 그래프들 복사해서 상어 움직이기
            qgraph2 = deepcopy(qgraph)
            qmove_graph2 = deepcopy(qmove_graph)
            
            # 원래 상어가 있던 곳은 0으로 비워주기
            qgraph2[sx][sy] = 0
            # 상어가 이동할 곳에 있는 물고기 번호
            temp = qgraph2[nsx][nsy]
            # 상어가 이동할 곳에 있는 방향
            nsd = qmove_graph2[temp - 1][2]
            # 죽은 물고기 방향 -1로
            qmove_graph2[temp - 1][2] = -1
            # 상어가 움직인 위치 표시
            qgraph2[nsx][nsy] = -1
            
            # 움직인 위치를 기준으로 생성된 그래프들과 변수값을 다시 q에 넣어주기
            q.append((qgraph2, qmove_graph2, [nsx, nsy, nsd], qscore + temp))
            # 상어가 움직였다면 flag는 False로
            flag = False
            
    # flag가 True라면 상어가 더 이상 못 움직이는 경우
    if flag:
        ans = max(ans, qscore)

print(ans)