- 출처 : [[이것이 코딩 테스트다 with Python] 33강 서로소 집합 자료구조
](https://www.youtube.com/watch?v=Ha0w2dJa2Nk&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=33)

#### 서로소 집합

공통 원소가 없는 두 집합

![Image](https://i.imgur.com/hnnkhFD.png)

### 서로소 집합 자료구조

- 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조

- 서로소 집합 자료구조는 두 종류의 연산을 지원한다

    - 합집합(Union): 두 개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
    - 찾기(Find): 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산

### 서로소 집합 자료구조: 동작 과정 살펴보기

- 처리 방법 (하지만, 개인적으로 이 표현이 이해 잘 안돼서, 그냥 아래 예시 보면서 이해하는 게 빠름)
  - i) A와 B 노드가 연결되어 있을 때
    - a) A와 B의 루트노드가 a, b 라고 하자
    - b) a와 b중 a가 더 크다면 a의 부모노드를 b로 설정
  - ii) i) 반복

- 처리할 연산들: 𝑈𝑛𝑖𝑜𝑛(1,4), 𝑈𝑛𝑖𝑜𝑛(2,3), 𝑈𝑛𝑖𝑜𝑛(2,4), 𝑈𝑛𝑖𝑜𝑛(5,6)


- [초기 단계] 노드의 개수 크기의 부모 테이블을 초기화한다

![Image](https://i.imgur.com/h32lgZk.png)

- [Step 1] 노드 1과 노드 4의 루트 노드를 각각 찾는다. 현재 루트 노드는 각각 1과 4이므로 더 큰 번호에
해당하는 루트 노드 4의 부모를 1로 설정한다

![Image](https://i.imgur.com/2WtjTRO.png)

- [Step 2] 노드 2과 노드 3의 루트 노드를 각각 찾는다. 현재 루트 노드는 각각 2와 3이므로 더 큰 번호에
해당하는 루트 노드 3의 부모를 2로 설정한다

![Image](https://i.imgur.com/Gebgxe4.png)


- [Step 3] 노드 2과 노드 4의 루트 노드를 각각 찾는다. 현재 루트 노드는 각각 2와 1이므로 더 큰 번호에
해당하는 루트 노드 2의 부모를 1로 설정한다

![Image](https://i.imgur.com/TmzW43Q.png)

- [Step 4] 노드 5과 노드 6의 루트 노드를 각각 찾는다. 현재 루트 노드는 각각 5와 6이므로 더 큰 번호에
해당하는 루트 노드 6의 부모를 5로 설정한다

![Image](https://i.imgur.com/qAMYoLB.png)

- 결론 : 연결성을 통해 쉽게 집합 형태를 확인할 수 있음.

![Image](https://i.imgur.com/5rEUyiD.png)

## 파이썬을 통한 구현 방법

```python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x
```

```python
# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
```

```python
# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력하기
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')
```

- 하지만, 위의 사례의 경우 시간 초과가 날 수 있다.

### 서로소 집합 자료구조: 경로 압축

- 시간 초과 해결책으로, 찾기(Find) 함수를 재귀적으로 호출한 뒤에 부모 테이블 값을 바로 갱신한다

```python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
```