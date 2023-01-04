# [투포인터] 15565 귀여운 라이언 (백준, Python, 실버1)

- [출처](https://www.acmicpc.net/problem/15565)

```
총평 : 투포인터 개념 헷갈릴 때 예제로 한번 더 풀면 좋을 문제
```

## 문제
꿀귀 라이언 인형과, 마찬가지로 꿀귀인 어피치 인형이 N개 일렬로 놓여 있다. 라이언 인형은 1, 어피치 인형은 2로 표현하자. 라이언 인형이 K개 이상 있는 가장 작은 연속된 인형들의 집합의 크기를 구하여라.

## 입력
첫 줄에 N과 K가 주어진다. (1 ≤ K ≤ N ≤ 106)

둘째 줄에 N개의 인형의 정보가 주어진다. (1 또는 2)

## 출력
K개 이상의 라이언 인형을 포함하는 가장 작은 연속된 인형들의 집합의 크기를 출력한다. 그런 집합이 없다면 -1을 출력한다.

## 예제 입력 1
10 3

1 2 2 2 1 2 1 2 2 1

## 예제 출력 1
6

## 풀이

```python
# 입력 값 받기
n, k = map(int, input().split())
data = list(map(int, input().split()))
ans = float('inf')

# 끝 포인터, 라이언 개수, 선택인형 개수
end, cnt, dolls = 0, 0, 0

for start in range(n):
    # end를 가능한 만큼 이동시키기
    while cnt < k and end < n:
        dolls += 1
        # 라이언 있을 때 카운트 증가
        if data[end] == 1:
            cnt += 1
        end += 1
        
    if cnt == k and ans > dolls:
        ans = dolls

    if data[start] == 1:
        cnt -= 1

    # start가 하나 움직여서 전체 수 줄어듦    
    dolls -= 1
    

print(ans if ans != float('inf') else -1)
```