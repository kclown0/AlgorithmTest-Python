str = input()
result = 1

if len(str) == 1:
    print(1)

elif str[0] == str[-1]:
    for i in range(1,len(str)//2):
        if str[i] == str[-i-1]:
            result += 1

    if result == len(str)//2:
        print(1)
    else:
        print(0)

else:
    print(0)
    
# 정수 몫 연산자 - //
# index 기준 비교
# [0 -1], [1,-2], [2,-3], ...