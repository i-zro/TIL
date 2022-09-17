import sys
import heapq
input = sys.stdin.readline
V, E = map(int, input().split())
start = int(input())    #   시작점
INF = int(1e9)  #   무한대 수
weights = [INF] * (V)    #   방문하지 않은 곳 찾으려고
graph = [[] for _ in range(V)]
for e in range(E):
    u, v, w = map(int, input().split())
    graph[u-1].append((v-1, w))
    
q = []
heapq.heappush(q, (0, start-1))   #시작점 가중치(0) 넣어주기
weights[start-1] = 0

while q:
    weight, node = heapq.heappop(q)   #   q에서 정점과 가중치 빼줌
    
    # INF가 아닌 경우니까 이미 방문한 것 = 셀 필요X
    if weights[node] < weight:
        continue
    
    # node와 연결 된 정점? 
    # next = (연결 정점, 가중치)
    for next in graph[node]:
        cost = weights[node] + next[0]  # 가중치
        if cost < weights[next[1]]:
            weights[next[1]] = cost
            heapq.heappush(q, (next[1], cost))
            
for i in range(len(weights)):
    if weights[i] == INF:
        print("INF")
    else:
        print(weights[i])