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
5 3 6
0 2
1 2
2 2
3 2
4 2
4 0 """)
answer=(
"""5\n1
2"""
    )
# print(answer)

from itertools import combinations
from collections import deque
import copy
def solution():
    test_case = int(input())
    for t in range(test_case):
        m, n, k = map(int, input().split())
        farm = [i ]

for T in range(TEST_CASE): 
    print('\033[95m'+"테스트 케이스 %d"%(T+1)+ '\033[0m')
    solution()
    print('\033[91m'+"정답"+ '\033[0m')
    print(answer.split('\n')[T])


# for _ in range(n):
#     print(input().split())
# from itertools import combinations
# from collections import deque

