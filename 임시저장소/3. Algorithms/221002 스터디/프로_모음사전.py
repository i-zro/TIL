def solution(word):
    answer = 0
    
    _dict = {}
    _dict["A"]=[1, 1, 1, 1, 1]
    _dict["E"]=[782, 157, 32, 7, 2]
    _dict["I"]=[1563, 313, 63, 13, 3]
    _dict["O"]=[2344, 469, 94, 19, 4]
    _dict["U"]=[3125, 625, 125, 25, 5]
    
    for _index, _word in enumerate(word) :
        answer += _dict[_word][_index];
        
    return answer