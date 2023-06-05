def solution(numer1, denom1, numer2, denom2):

    num = (numer1*denom2)+(numer2*denom1) 
    denom = denom1*denom2
    
    answer = [num, denom]

    for i in range(min(num, denom), 0, -1):
        if num % i == 0 and denom % i == 0:
            answer = num / i, denom / i
            break
    
    return answer