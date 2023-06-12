def solution(a, b):
    ab = str(a)+str(b)
    ba = str(b)+str(a)
    ab_list=[int(ab),int(ba)]
    answer = max(ab_list)
    return answer