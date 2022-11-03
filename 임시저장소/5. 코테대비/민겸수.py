mks = input()  #   민겸수 받아옴

def solution(mks):
    minm = ''   # 민겸수 최솟값
    maxm = ''   # 민겸수 최댓값
    mnum = 0    # 결과값
    
    for m in mks:
        if m == 'M':
            mnum += 1
        else:
            if not mnum:    #   K가 맨앞이야.
                minm += '5'
                maxm += '5'
            else:
                minm += '1' + '0' * (mnum-1)
                minm += '5'
                maxm += '5' + '0'*mnum                
            mnum = 0
    if mnum:
        minm += '1' + '0' * (mnum-1)
        maxm += '1'*mnum
    
    print(maxm)        
    print(minm)

solution(mks)