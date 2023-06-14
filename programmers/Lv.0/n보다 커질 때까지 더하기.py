def solution(numbers, n):
    sum_num = 0
    for i in range(len(numbers)):
        if sum_num <= n:
            sum_num += numbers[i]
    return sum_num