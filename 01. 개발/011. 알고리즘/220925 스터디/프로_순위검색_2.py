# 2차시도 : set 이용 - 정확성만 통과

def solution(info, query):
    answer = []
    
    for q in query:
        # query 조건 정리 리스트
        condition = list(qq.strip() for qq in q.replace('and', '').replace('  ',' ').split(' '))
        condition_items = set(condition[:-1]) - {'-'}
        condition_score = int(condition[-1])

        num = 0
        
        for i in info:
            participant = list(ii.strip() for ii in i.split(' '))
            participant_items = set(participant[:-1])
            participant_score = int(participant[-1])
            
            if participant_score >= condition_score:
                if len(condition_items) == len(condition_items & participant_items):
                    num += 1
                    
        answer.append(num)
        
    return answer