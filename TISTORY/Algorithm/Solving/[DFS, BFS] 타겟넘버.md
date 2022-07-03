### 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/43165

## 문제 설명
n개의 음이 아닌 정수들이 있습니다. 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

## 제한사항
주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
각 숫자는 1 이상 50 이하인 자연수입니다.
타겟 넘버는 1 이상 1000 이하인 자연수입니다.

## 입출력 예
numbers	target	return
[1, 1, 1, 1, 1]	3	5
[4, 1, 2, 1]	4	2
입출력 예 설명
### 입출력 예 #1

문제 예시와 같습니다.
<table class="table">
        <thead><tr>
<th>numbers</th>
<th>target</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>[1, 1, 1, 1, 1]</td>
<td>3</td>
<td>5</td>
</tr>
<tr>
<td>[4, 1, 2, 1]</td>
<td>4</td>
<td>2</td>
</tr>
</tbody>
      </table>

### 입출력 예 #2

+4+1-2+1 = 4
+4-1+2-1 = 4
총 2가지 방법이 있으므로, 2를 return 합니다.

## DFS 풀이
### 풀이과정
해당 문제를 풀기 위해서 아래 그림과 같이 음수값, 양수값으로 가지치기를 한 이후, 가지치기 끝에서 모든 값을 더해야함을 알 수 있다.

<span style='background-color: #ffdce0'>이렇게 모든 '경우의 수' (경로)를 구해야하는 느낌일 때 DFS를 사용한다.</span>
![Image](https://i.imgur.com/5mhv6bb.png)

- ans += dfs(numbers, target, depth + 1) => dfs([4, 1, 2, 1], 4, 1) ... => dfs([4,1,2,1], 4, 4) = return 0

- numbers[0] * = -1 => [-4, 1, 2, 1] 이렇게 음수 경우의 수 만들어주는 역할

- ans += dfs(numbers, target, depth + 1) => dfs([4, 1, 2, 1], 4, 1) ... => dfs([4,-1,2,-1], 4, 4) = 1

-  dfs 깊이 최종까지 갔을 때, 0 반환 또는 1 반환 파악해서 ans 변수에 더해주기 => 몇 가지 경우인 지 알 수 있음. 

![Image](https://i.imgur.com/vIWlvqu.png)

```python
def solution(numbers, target):
    answer = 0
    answer = dfs(numbers, target, 0)
    return answer

def dfs(numbers, target, depth):
    ans = 0
    if len(numbers) == depth:
        if sum(numbers) == target:
            return 1
        return 0
    else:
        ans += dfs(numbers, target, depth + 1)
        numbers[depth] *= -1    # 음수인 경우의 수 만들기
        ans += dfs(numbers, target, depth + 1)
        return ans
    
```

## BFS 풀이
### 풀이과정
해당 과정에서 끝까지 경로를 탐색하는 게 아니라, 바로바로 하나씩 빼거나 더해줘서 경로를 하나씩 더해갔다.

```python
def solution(numbers, target):
    answer = 0
    answer = bfs(numbers, target)
    return answer

from collections import deque
def bfs(numbers, target):
    ans = 0
    current_q = deque()
    current_q.extendleft([numbers[0], -numbers[0]])
    next_q = deque()
    for t in numbers[1:]:    
        for num in current_q:
            next_q.appendleft(num + t)
            next_q.appendleft(num - t)
        current_q = deque()
        current_q.extendleft(next_q)
        next_q = deque()
    for c in current_q:
        if c == target:
            ans += 1
            
    return ans
```