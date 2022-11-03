## 출처
https://www.acmicpc.net/problem/5525

## 문제
N+1개의 I와 N개의 O로 이루어져 있으면, I와 O이 교대로 나오는 문자열을 PN이라고 한다.

P1 IOI
P2 IOIOI
P3 IOIOIOI
PN IOIOI...OI (O가 N개)
I와 O로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S안에 PN이 몇 군데 포함되어 있는지 구하는 프로그램을 작성하시오.

## 입력
첫째 줄에 N이 주어진다. 둘째 줄에는 S의 길이 M이 주어지며, 셋째 줄에 S가 주어진다.

## 출력
S에 PN이 몇 군데 포함되어 있는지 출력한다.

## 제한
1 ≤ N ≤ 1,000,000
2N+1 ≤ M ≤ 1,000,000
S는 I와 O로만 이루어져 있다.
서브태스크
번호	배점	제한
1	50	
N ≤ 100, M ≤ 10 000.

2	50	
추가적인 제약 조건이 없다.

### 예제 입력 1 
1
13
OOIOIOIOIIOII
### 예제 출력 1 
4
OOIOIOIOIIOII
OOIOIOIOIIOII
OOIOIOIOIIOII
OOIOIOIOIIOII
### 예제 입력 2 
2
13
OOIOIOIOIIOII
### 예제 출력 2 
2

### 풀이
### 문제풀이

1. 50%
첫 번째는 그냥 반복문을 일일이 돌아서 풀려고 했다.

```python
import sys
input = sys.stdin.readline

n = int(input())
l = int(input())
S = input()

def solution(n):
    # return n
    ans = 0
    P = 'I' + 'OI' * n
    
    for s in range(l):
        if S[s:s+len(P)] == P:

            # print(S[s:s+len(P)])
            ans+=1
            continue
    return ans
    
print(solution(n))
```

2. 100%
지섭님의 조언을 받아(치환)
치환하고 반복문을 줄여서 돌리니까 잘 돌아갔다!
반복되는 문자열을 `치환`해서 줄이는 것도 하나의 방법!

```python
import sys
input = sys.stdin.readline

n = int(input())
l = int(input())

def solution(n, S):
    from collections import deque

    ans = 0
    P = 'I' + 'OI' * n
    S = S.replace(P, 'P')
    # print(S)

    A = "OI"
    S = S.replace(A, "A")
    # print(S)
    
    s = 0
    while s < len(S):
        # print(s, len(S))
        # print("P", S[s])

        if S[s] == 'P':
            s+=1
            ans += 1
            while s < len(S):
                if S[s] == 'A':
                    ans+=1
                    s+=1
                    # print(s, ans)
                    
                elif S[s : s+2] == 'OP':
                    ans += (n+1)
                    # print(s, ans)
                    s+=2
                    
                else:
                    break
            continue
        else:
            s+=1
                
    print(ans)
        
S = input()
solution(n, S)

```

3. 구글 풀이
구글에서 상위 블로그의 풀이방법이 내 풀이와 달라서 풀이법을 이해한 후 직접 풀어봤다.

ioi 반복문자열이라서 연속된 i의 인덱스차이가 2라는 것을 이용한다.
해당 반복이 주어진 반복횟수보다 같거나 클때부터 세어나가면 연속된 반복횟수가 얼마인지 구할 수 있다.

```python
import sys
input = sys.stdin.readline

n = int(input())
l = int(input())

def solution(n, S):
    s_stack = [i+1 for i, s in enumerate(S[1:l]) if s == 'I']   # 0과 l에는 있어도 소용 X
    cnt = 0
    ans = 0

    for s in range(1, len(s_stack)):
        if s_stack[s] - s_stack[s-1] == 2:
            cnt+=1
        else:   # 2차이 아니라서 연속성 끊김
            cnt = 0
        
        if cnt >= n:
            ans+=1  
            
    print(ans)      
        
S = input()
solution(n, S)
```