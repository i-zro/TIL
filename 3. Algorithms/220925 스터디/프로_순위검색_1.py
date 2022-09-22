# 정확성만 통과

def solution(info, query):
    answer = []
    
    for q in query:
        # query 조건 정리 리스트
        condition = list(qq.strip() for qq in q.replace('and', '').replace('  ',' ').split(' '))
        num = 0
        
        for i in info:
            participant = list(ii.strip() for ii in i.split(' '))
            for e,(c,p) in enumerate(zip(condition, participant)):
                if c == '-':
                    continue
                if c != p and not (c.isdigit() and int(c) <= int(p)):
                    break
                if e == len(condition)-1:
                    num += 1
                    
        answer.append(num)
        
    return answer