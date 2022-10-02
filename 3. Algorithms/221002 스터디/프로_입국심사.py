"""
1. 최소 시간(start)과 가장 비효율적으로 구했을 때의 시간(end)을 구한다.
2. 둘의 중간 시간에서 각 심사위원이 몇 명의 사람의 심사를 거칠 수 있는지 구한다. (mid)
3. start 와 end가 같아질 때, 이 값이 최소 시간이다. 

"""

def binary_search(n, times):
    times.sort()
    
    start = 0
    # 걸리는 최대 시간
    end = max(times) * n

    while start < end:
        # 중간값
        mid = (start + end) // 2
        total = 0
        
        for _times in times:
            total += mid // _times
            
            # 모든 심사관을 거치지 않아도 mid분 동안 n명 이상의 심사를 할 수 있다면 반복문을 나간다. (이 부분처음에 안 넣음. 안 넣어도 통과하긴 함.)
            if total >= n:
                break

        if total >= n:
            end = mid
        else:
            start = mid + 1

    return start

def solution(n, times):
    answer = binary_search(n, times)
    return answer