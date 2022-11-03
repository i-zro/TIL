from collections import defaultdict

R, C, N = map(int, input().split())

all = [[i, j] for j in range(C) for i in range(R)]
print(all)