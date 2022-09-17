# n, m = map(int, input().split())

# from itertools import permutations

# ans_temp = list(permutations([i for i in range(1, n+1)], m))

# for ans in ans_temp:
#     for a in ans:
#         print(a, end=' ')
#     print('')

def nAndM(depth, n, m):
    # 탈출조건 : 트리 깊이가 주어진 배열값과 같을 때
    if depth == m:
        print(' '.join(map(str, answer)))   # join + map
        
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            answer.append(i)
            nAndM(depth+1, n, m)
            visited[i] = False
            answer.pop()

n, m = map(int, input().split())
visited = [False] * (n+1)
answer = []

nAndM(0, n, m)
   