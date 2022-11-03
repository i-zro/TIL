![Image](https://i.imgur.com/gExvnal.png)
![Image](https://i.imgur.com/dKZBYjZ.png)
![Image](https://i.imgur.com/rpd8EM9.png)

```python
def solution(X, Y):
    from collections import deque

    q = deque([x for x in X])
    y_q = deque([y for y in Y])
    y_visited = [False for yyy in range(len(Y))]

    common_items = []
    # print(q)
    while q:
        item = q.popleft()
        for y_num, yy in enumerate(y_q):
            if yy == item and not y_visited[y_num]:
                common_items.append(yy)
                y_visited[y_num] = True
                break
    
    if not len(common_items):
        return "-1"

    return "0" if sum(list(map(int, common_items))) == 0 else ''.join(sorted(common_items)[::-1])

```

![Image](https://i.imgur.com/OkpRsXT.png)

```python
def solution(want, number, discount):
    answer = 0
    dc_sum = [0 for i in range(len(discount))]
    # print(dc_sum)

    for d_idx, d in enumerate(discount):
        for w_idx, w in enumerate(want):
            if w == d:
                if number[w_idx] > 0:
                    dc_sum[d_idx] += 1
        print(dc_sum)
        if dc_sum[d_idx] == 10:
            return len(discount) - 1 - d_idx
            
        if d_idx+1 != len(dc_sum):
            dc_sum[d_idx+1] = dc_sum[d_idx]
        
    return answer

```

![Image](https://i.imgur.com/viSeVbe.png)

```python
def solution(order):
    from collections import deque

    order_q = deque(order)
    stack_q = deque(list())
    nums = deque([i for i in range(1, len(order)+1)])
    answer = 0
    while order_q:
        item = order_q.popleft()
        if stack_q and stack_q[-1] == item:
            stack_q.pop()
            answer+=1
            continue
        while nums:
            n_item = nums.popleft()

            if n_item == item:
                answer+=1
                break;
            else:
                stack_q.append(n_item)

            if(len(nums)==0):
                return answer

            


    for n in range(1, len(order)+1):
        while order_q:
            item = order_q.popleft()
            if n != item:
                stack_q.append(n)
    return answer

```

![Image](https://i.imgur.com/FjoGOY9.png)

```python
def solution(beginning, target):
    from itertools import permutations
    import copy
    from collections import deque

    answer = 0
    temp = deque([beginning])

    while temp:
        beginning = temp.popleft()

        # print(beginning)
        for idx, b in enumerate(beginning):
            # print(b)
            b_temp = copy.deepcopy(beginning)
            # print(b_temp)
            b_temp[idx] = [1 << i for i in b]
            print(b_temp)
            # temp.append(b_temp)

        if len(temp) == 1:
            break

        # for k in range(len(beginning)):
        #     b_temp = copy.deepcopy(beginning)
        #     for kk in range(len(beginning)):
        #         b_temp[kk][k] = 1 << b_temp[kk][k]
        #     temp.append(b_temp)
        # print(temp)

    return answer
```
![Image](https://i.imgur.com/6wNpZYC.png)
