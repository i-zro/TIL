def solution(number):
    answer = 0

    # 숫자 배열 정렬
    number.sort()

    # 한 개의 수를 우선 선택하고, 나머지 두 수를 선택해서 합한 후, 서로 빼줘서 0 되는 경우 찾기
    for i in range(len(number) - 2):
        left, right = i+1, len(number) - 1  # 극단의 수 2개 선택
        goal = -number[i]  # 한 개 수 선택하고, 그 수를 0으로 만들기 위한 goal 선택
        max_idx = len(number)

        while left < right:
            tmp = number[left] + number[right]
            # 1. 합한 수가 goal보다 작을 때
            if tmp < goal:
                left += 1

            # 2. 합한 수가 goal일 때 (target)
            elif tmp == goal :
                # 2-1.
                if number[left] == number[right]:
                    answer += right - left

                # 2-2.
                else:
                    if max_idx > right:
                        # 끝 값을 끝 right에 맞춰주기
                        max_idx = right

                        while number[right] == number[max_idx-1]:   # right에 있는 같은 수들 찾기
                            max_idx -= 1
                    answer += right - max_idx + 1

                # left 한 칸 밀어주기
                left += 1

            # 3. 합한 수가 goal보다 작을 때
            else:
                right -= 1                       
    return answer
