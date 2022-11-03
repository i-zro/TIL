# 1. 데이터 받아오기 : 폭탄일 때 3초(터지는 초)로 받고 아닐 때 0초로 받기
import sys
from collections import deque

input = sys.stdin.readline
R, C, N = map(int, input().split())
maps = []
# 현재 폭탄 위치 알기
find_bomb = lambda li: [(i, j) for j in range(C) for i in range(R) if li[i][j]]  


for r in range(R):
    maps.append([])
    row = input()
    # print(row)
    for rw in row:
        if rw == 'O':
            maps[r].append(3)
        else:
            maps[r].append(0)
# print(maps)


# 2. 폭탄 채우기 : 현재 시간
def fill_bombs(time):
    global maps
    for row_num in range(len(maps)):
        maps[row_num] = [(time+3) if not i else i for i in maps[row_num]]


# 4. 폭탄 터지기
def explode_bombs(time):
    global maps
    movin = [[-1,0], [1,0], [0,-1], [0,1]]
    for mov in movin:
    

# 3. 0 아니면 O 출력, 0이면 . 출력
for row in maps:
    print("".join(['O'  if i else '.' for i in row]))