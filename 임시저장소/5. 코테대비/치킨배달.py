from collections import defaultdict


N, M = map(int, input().split())

nmaps = []
chicks = [] # 치킨집 수
homes = defaultdict(list) # 집의 수

for _ in range(N):
    temp = list(map(int, input().split()))
    chicks.extend([[_, i] for i, t in enumerate(temp) if t == 2])
    homes[_].extend([i for i, t in enumerate(temp) if t ==1])

# print(homes)
from itertools import combinations
chickens = list(combinations(chicks, M))

temp = [0, 0, 0]
min_sum = float("inf") # 가장 적은 거리 내는 치킨집 조합
for chick in chickens:
    min_dist_temp = 0 # 해당 치킨 집 조합일 때 총 거리
    break_point=False
    for k,v in homes.items():
    #     print(k, v)
        for vi in v:
            # 3가지 치킨집 중 가장 적은 거리를 내는 곳까지의 거리
            min_temp = min([abs(k-kidx) + abs(vi-videx) for kidx, videx in chick])
            min_dist_temp += min_temp
            
            if min_sum < min_dist_temp:
                break_point = True
                break
        if break_point:
            break
    if not break_point:
        min_sum = min_dist_temp
                
print(min_sum)
            
    
        
    
    