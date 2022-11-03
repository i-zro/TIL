1. 교집합
```
set1 = set([1,2,3,4,5,6])
set2 = set([3,4,5,6,8,9])

print(set1 & set2)
print(set1.intersection(set2))

{3, 4, 5, 6}
{3, 4, 5, 6}
```

2. 합집합

```
set1 = set([1,2,3,4,5,6])
set2 = set([3,4,5,6,8,9])


print(set1 | set2)
print(set1.union(set2))


{1, 2, 3, 4, 5, 6, 8, 9}
{1, 2, 3, 4, 5, 6, 8, 9}
```

3. 차집합

```
set1 = set([1,2,3,4,5,6])
set2 = set([3,4,5,6,8,9])


print(set1 - set2)
print(set1.difference(set2))

{1, 2}
{1, 2}
```
4. 대칭 차집합

```
set1 = set([1,2,3,4,5,6])
set2 = set([3,4,5,6,8,9])

print(set1 ^ set2)

{1, 2, 8, 9}
```
5. 집합 추가와 제거

```
set1 = set([1,2,3,4,5,6])
set1.update([7,8,9])         # update
print(set1)

set1.remove(9)               # remove
print(set1)
-------------------------------------------
{1, 2, 3, 4, 5, 6, 7, 8, 9} {1, 2, 3, 4, 5, 6, 7, 8}
```